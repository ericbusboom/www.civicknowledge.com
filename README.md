# www.civicknowledge.com

Static Hugo site converted from WordPress.

## Development
```bash
just dev    # or: hugo server --buildDrafts
just build  # or: hugo --minify --buildDrafts
```

## Deployment
Pushes to `main` trigger GitHub Actions → GitHub Pages.

## How the content was made

Converted from WordPress blog 3 by `_tools/wp2hugo.py` (personal-websites
repo), then fixed up by [migration/fix_content.py](migration/fix_content.py):
pages at their WordPress URLs, posts typed `post`, old-host links made
relative, upload links pointed at files in `static/uploads/`. Images from
blog 4 (insights.civicknowledge.com) were recovered from the June 2026
WordPress backup in `s3://backup.busboom.org`. Short-link redirects are in
`_infra/websites.busboom.org/civicknowledge.caddy` in the parent repo.
