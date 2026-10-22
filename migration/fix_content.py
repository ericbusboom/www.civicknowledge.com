#!/usr/bin/env python3
"""Fix up www.civicknowledge.com after the WordPress (blog 3) conversion.

wp2hugo.py wrote every page flat into content/, so nested page URLs were
lost and two pages with the slug "consultation" overwrote each other. This
script, run from the personal-websites repo root:

  1. regenerates the pages from the WXR export at their WordPress URLs
     (`url:` front matter); the static front page becomes content/_index.md,
     the WordPress posts page becomes the /posts/ list
  2. marks blog posts `type: "post"` so lists and Recent Posts find them
  3. rewrites links to the old hosts (www./insights.civicknowledge.com, the
     sandiegodata test host) to site-relative or current URLs
  4. points /uploads/ links at files that exist in static/; files that are
     gone are marked "(no longer available)" and images are dropped
  5. removes WordPress shortcode leftovers ([icon ...], [code] blocks)

    uv run --with html2text --with python-dateutil \\
        python3 www.civicknowledge.com/migration/fix_content.py \\
        _export/blog3/<file>.xml www.civicknowledge.com
"""
import argparse
import csv
import html
import io
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "_tools"))
import wp2hugo  # noqa: E402

NS = wp2hugo.NS
SKIP_SLUGS = wp2hugo.SKIP_PAGES
# Pages that only held a plugin shortcode with no text of their own
EMPTY_PAGES = {"privacy", "terms-of-service"}
# Pages whose slug clashes with another page: post_id -> file name
FILE_NAMES = {"518": "consultation-commercial"}


def text(el, path):
    found = el.find(path, NS)
    return (found.text or "") if found is not None else ""


def url_path(link):
    return "/" + link.split("://", 1)[1].split("/", 1)[1]


def frontmatter(fields):
    lines = ["---"]
    for k, v in fields.items():
        if v is None:
            continue
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(json.dumps(x) for x in v)}]")
        elif isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        else:
            lines.append(f"{k}: {json.dumps(v)}")
    lines.append("---")
    return "\n".join(lines)


def post_lists(content, cats):
    """coblocks/posts and atomic-blocks post grids -> post-list shortcode."""
    found = []

    def coblocks(m):
        args = json.loads(m.group(1))
        names = [cats.get(c.get("slug"), c.get("name")) for c in args.get("categories", [])]
        attrs = 'section="post"' + (f' category="{names[0]}"' if names else "")
        found.append("{{< post-list " + attrs + " >}}")
        return f"\n\nPOSTLIST{len(found) - 1}TOKEN\n\n"

    content = re.sub(r"<!-- wp:coblocks/posts (\{.*?\}) /-->", coblocks, content)
    return content, found


def regenerate_pages(xml_path, content_dir):
    root = ET.parse(xml_path).getroot()
    channel = root.find("channel")
    cats = {text(c, "wp:category_nicename"): html.unescape(text(c, "wp:cat_name"))
            for c in channel.findall("wp:category", NS)}
    items = channel.findall("item")
    pages = [i for i in items if text(i, "wp:post_type") == "page" and text(i, "wp:status") == "publish"]
    posts = [i for i in items if text(i, "wp:post_type") == "post" and text(i, "wp:status") == "publish"]

    for it in pages:
        old = content_dir / f"{text(it, 'wp:post_name')}.md"
        if old.exists():
            old.unlink()

    written = 0
    for it in pages:
        slug = text(it, "wp:post_name")
        pid = text(it, "wp:post_id")
        if slug in SKIP_SLUGS or slug in EMPTY_PAGES:
            continue
        path = url_path(it.find("link").text)
        fields = {
            "title": html.unescape(it.find("title").text or ""),
            "date": wp2hugo.dateparser.parse(text(it, "wp:post_date")).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
            "draft": False,
            "author": text(it, "dc:creator") or None,
        }
        if slug == "front-page":
            out = content_dir / "_index.md"
            fields["aliases"] = ["/front-page/", "/home/"]
        elif slug == "home":
            continue  # a 10-post grid; the front page lists recent posts now
        elif slug == "posts":
            out = content_dir / "posts" / "_index.md"
        else:
            fields["url"] = path
            out = content_dir / f"{FILE_NAMES.get(pid, slug)}.md"

        raw = it.find("content:encoded", NS).text or ""
        raw, lists = post_lists(raw, cats)
        body = wp2hugo.convert_html_to_markdown(raw, 3)
        for i, sc in enumerate(lists):
            body = body.replace(f"POSTLIST{i}TOKEN", sc)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(frontmatter(fields) + "\n\n" + body + "\n")
        written += 1

    marked = 0
    for it in posts:
        md = content_dir / f"{text(it, 'wp:post_name')}.md"
        if md.exists():
            s = md.read_text()
            if "\ntype:" not in s.split("\n---", 1)[0]:
                md.write_text(s.replace("\ndraft: false\n", '\ndraft: false\ntype: "post"\n', 1))
                marked += 1
    return written, marked


def site_paths(site):
    out = subprocess.run(["hugo", "list", "all", "-s", str(site)],
                         capture_output=True, text=True, check=True).stdout
    paths = {"/", "/posts/", "/categories/", "/tags/"}
    for row in csv.DictReader(io.StringIO(out)):
        paths.add(re.sub(r"^https?://[^/]+", "", row["permalink"]))
    return paths


OLD_HOST = re.compile(r"https?://(www\.|insights\.)?civicknowledge\.com(/[^\s)\"'<>\]]*)?")
SDD_TEST = re.compile(r"https?://sandiegodata\.wordpress\.civicknowledge\.com(/[^\s)\"'<>\]]*)?")
# Old paths with no page of the same name
PATH_MAP = {"/consultation/initial-consultation/": "/consultation/book-a-meeting/"}


def relink(site, content_dir):
    paths = site_paths(site)
    by_slug = defaultdict(list)
    for p in paths:
        by_slug[p.rstrip("/").rsplit("/", 1)[-1]].append(p)

    def resolve(path):
        path = path or "/"
        path, _, frag = path.partition("#")
        if path.startswith("/wp-content/uploads/sites/"):
            return re.sub(r"^/wp-content/uploads/sites/", "/uploads/", path)
        if not path.endswith("/"):
            path += "/"
        path = PATH_MAP.get(path, path)
        if path not in paths:
            hits = by_slug.get(path.rstrip("/").rsplit("/", 1)[-1], [])
            if len(hits) != 1:
                return None
            path = hits[0]
        return path + ("#" + frag if frag else "")

    n, missing = 0, Counter()
    for md in content_dir.rglob("*.md"):
        old = md.read_text()

        def sub(m):
            nonlocal n
            new = resolve(m.group(2))
            if new is None:
                missing[m.group(0)] += 1
                return m.group(0)
            n += 1
            return new

        new = OLD_HOST.sub(sub, old)
        new = SDD_TEST.sub(lambda m: "https://www.sandiegodata.org" + (m.group(1) or "/"), new)
        if new != old:
            md.write_text(new)
    return n, missing


# jetpack size arguments (?resize=, ?fit=) are part of these matches
UPLOAD = re.compile(r"/uploads/[^\s)\"'<>#]+")
IMAGE = re.compile(r"!\[[^\]]*\]\(<?(/uploads/[^)>]+)>?\)")
LINK = re.compile(r"\[(?P<text>[^\]]*)\]\(<?(?P<url>/uploads/[^)>]+)>?\)")
SPLIT = re.compile(r"(\(<?/uploads/[^\s)>]*)\n([^\s)>]+)")


def fix_media(site, content_dir):
    static = site / "static"
    by_rest, by_name = defaultdict(set), defaultdict(set)
    for f in (static / "uploads").rglob("*"):
        if f.is_file():
            url = "/" + str(f.relative_to(static))
            by_rest[re.sub(r"^/uploads/(\d+/)?", "", url)].add(url)
            by_name[f.name].add(url)

    def fix(url):
        url = url.split("?")[0]
        if (static / url.lstrip("/")).is_file():
            return url
        for hits in (by_rest.get(re.sub(r"^/uploads/(\d+/)?", "", url)), by_name.get(url.rsplit("/", 1)[-1])):
            if hits:
                return sorted(hits)[0]  # duplicates are copies of the same upload
        return None

    stats = Counter()
    for md in content_dir.rglob("*.md"):
        old = md.read_text()
        new = old
        while SPLIT.search(new):
            new = SPLIT.sub(r"\1\2", new)

        def image(m):
            if fix(m.group(1)) is None:
                stats["image removed"] += 1
                return ""
            return m.group(0)

        def link(m):
            if fix(m.group("url").split("#")[0]) is None:
                stats["link removed"] += 1
                return f"{m.group('text')} (no longer available)"
            return m.group(0)

        def remap(m):
            new_url = fix(m.group(0))
            if new_url and new_url != m.group(0):
                stats["link moved"] += 1
                return new_url
            return m.group(0)

        new = IMAGE.sub(image, new)
        new = LINK.sub(link, new)
        new = UPLOAD.sub(remap, new)
        if new != old:
            md.write_text(new)
    return stats


CODE = re.compile(r"\[code\] *\n?(.*?)\n?[ \t]*\[/code\]", re.S)


def cleanup(content_dir):
    def fence(m):
        lines = [l[4:] if l.startswith("    ") else l for l in m.group(1).split("\n")]
        return "```\n" + "\n".join(lines).rstrip() + "\n```"

    n = 0
    for md in content_dir.rglob("*.md"):
        old = md.read_text()
        new = re.sub(r"\[icon [^\]]*\] ?", "", old)
        new = CODE.sub(fence, new)
        if new != old:
            md.write_text(new)
            n += 1
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("wxr", type=Path)
    ap.add_argument("site", type=Path)
    args = ap.parse_args()
    content = args.site / "content"

    written, marked = regenerate_pages(args.wxr, content)
    print(f"pages written: {written}; posts marked type post: {marked}")
    n, missing = relink(args.site, content)
    print(f"old-host links rewritten: {n}; unresolved: {dict(missing)}")
    print("media:", dict(fix_media(args.site, content)))
    print(f"files cleaned of shortcodes: {cleanup(content)}")


if __name__ == "__main__":
    main()
