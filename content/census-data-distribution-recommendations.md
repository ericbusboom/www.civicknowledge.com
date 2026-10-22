---
title: "Census Data Distribution Recommendations"
date: "2016-12-09T01:45:06+00:00"
draft: false
author: "eric"
url: "/papers/census-data-distribution-recommendations/"
---

As the single most important collection of demographic information nationwide, the annual American Community Survey and decennial Census datasets are so important that data analysts are willing to expend almost any level of effort to use them, and this willingness masks the significant effort required to use Census data in several important use cases. However, the difficulties in acquiring Census data are not fundamental, and some relatively small changes to metadata could make many use cases much easier, particularly bulk loading Census data into databases and accessing single files for analysis. This set of recommendations is drawn from experience in using Census data in both bulk and analysis on single tables, and will cover only those use cases. Other use cases, such as building tables for a single geography, or visualizing a measure for a collection of geographies are both managed well by other tools like American Fact Finder and Census Reporter. However, these visualization tools require bulk loading census data, so while the other tools’ use cases are not relevant to these recommendations, the experiences for building and maintaining those tools is.  It is clear from recent changes to the organization of the Census FTP directories that Census staff are interested in improving bulk access. We offer these recommendations in the hope of aiding that ongoing process of improvement. 

## **Why is Using Census Data Hard?**

Using Census data in bulk and extracting single tables are both hard for similar reasons: 

  * Substantial processing is required to extract a table from a sequence file.
  * Several separate files must be combined to make a useful dataset.
  * The datasets mixes all summary levels together, but analysts usually require only one. 
  * Metadata is spread across multiple files and is both redundant and inconsistent. 

Because of these issues, extracting tables from the bulk data requires a dozen steps, and creating automated extractions requires weeks of programming. The American Community Survey and Decennial Census data are used on a regular basis by tens of thousands of analysts, so making improvements to these issues would have a substantial nationwide benefit. 

## **Summary of Recommendations**

To address these issues, we recommend these changes, each of which is considered in detail at the end of the report:

  * Simplify data format
  * Normalize the metadata
  * Publish data in CSV format
  * Formally document geoid structure
  * Review and reconsider the use of fractional line numbers

In the remainder of this report, we will describe the current organization of the 2014 American Community releases, identify important issues, and offer suggestions for improvement. 

# 2014 Release

In April 2015, the data directory for the American community survey was re-organized, with a new, more consistent structure. This [new directory hierarchy](<http://www2.census.gov/programs-surveys/acs/summary_file/>) is more consistent at the top level, but earlier years of data do not have the same structure as later years. We’ll analyze the latest year, 2014, but earlier years should also be considered, since bulk loading earlier years is required to do multi-year comparisons. The following notes are for the files that are online under the URL path [http://www2.census.gov/programs-surveys/acs/summary_file/2014/](<http://www2.census.gov/programs-surveys/acs/summary_file/2014/>). At the top level, a release year directory has two directories: 

  * Data: the data directory
  * Documentation: documentation and metadata.


## **Data Directory**

Within the release year data directory are two sets of files, one for each release, (currently a 1-year and a 5-year release). The data is organized into sequence files, each of which holds data for one or more tables. The set of files for the 5-year release are:  

  * **5_year_by_state/: Directory of archives, per state. Each archive holds the sequence files for one state, including estimates, margins, and geofiles. **

 
    * **5_year_entire_sf/** : A single, large archive of all files. 

 
  * **5_year_seq_by_state/: Archives of traditional sequence files, broken out by state. Each archive holds data for one or more tables, for one state, and contains two sequence files, one for estimates and one for margins.**


  * 2014_5yr_Summary_FileTemplates.zip. An archive of template files, in Excel format. Each template file holds a single-line spreadsheet with the headers for a sequence file, and one for the geofile. 

  The second part of each year release is the documentation directory, which holds both documentation and metadata.  The directories for other release years are different, sometimes substantially different, although it does appear there have been recent efforts to normalize the structure across multiple years. The variations from year to year are a major impediment to using multi-year data. 

## **Metadata**

Metadata is split across multiple directories and files:

  * The data directories have File Templates, (2014_5yr_Summary_FileTemplates.zip), which hold the header lines for sequence files. 
  * The documentation/tech_docs directory has an appendix file, which describes the column positions for tables in the sequence files. 
  * The documentation/user_tools directory has two important metadata files: Table Shells, which gives the name, description, and “line number“ (related to column number) for columns in tables, and Table Number Lookup files, which also has table numbers, column lines, and sequence numbers. 

The most important metadata files are the Table Shells and Table Number lookup files.  The File Templates are single-line excel files that hold only the column headings for their corresponding data files.  The Table Shells are Excel files with two worksheets. The two worksheets are almost identical, and redundant, except the second worksheet has values for the UniqueId column, where the first does not, and the first worksheet includes fractional line numbers to indicate intermediate table headings. It is unclear why these two worksheets were not combined into a single dataset; it may be that one table--the one with fractional line numbers--is intended for table display, and the second--without fractional line numbers--is to be used to describe the columns in tables.  The Table Number Lookup files have only one worksheet, but the information in the file overlaps substantially with both of the Table Shell worksheets, including table IDs and table and column titles. However, the Table Number Lookup files also have the sequence file number in which the table appears and the starting column number of the first table column in the sequence file.  These four metadata files have substantial overlaps, but they are also missing information. For instance, it is important to know which columns roll up to other columns, since every table has total and subtotal columns. But this information is only represented in the indentation of the column descriptions in the Table Shell files. It was included in one or two previous years as an “indent level” column, but not in years before or since. The loss of link between columns, to indicate parent/child relationships, is a significant loss of metadata. 

# Recommendations

## **Simplify Data Format**

There are a variety of issues related to the structure of files and their formatting. The major issues are: 

  * Sequence files are difficult to use.
  * Sequence files have many different summary levels
  * Too many files must be linked to be useful
  * Several linkage fields appear to be unused or redundant


### **Sequence Files**

The Sequence files are difficult to use. The sequence file structure appears to be a legacy from 9-track tape drives, combining multiple tables, up to a maximum of 255 columns, to reduce the number of tapes required. While this structure probably made data processing easier in the mainframe era, the structure is now an impediment to using the files. There are several difficulties with sequence files: 

  * They include multiple tables in each file, with metadata required to break them apart.
  * They don’t have a header row, so the column headings must be extracted from metadata
  * They have many summary levels in each file, while the typical analysis case is to use only one summary level, and they must be merged with the geofile to determine which rows to extract for a single summary level. 

Census data users are primarily interested in only one summary level at a time for a limited number of tables, and they can best use the data when it is immediately loadable into a spreadsheet program. These factors suggest that a preferable form for the data files is that of many files, each holding data for one table and one summary level, possibly broken into states for the smallest summary level areas.  However, the table data is nearly useless unless it is merged with the geofile to get geographic names and identifiers. The geofile is fairly large, but only a few columns are used for each summary level. If a data file has only one summary level, the associated geofile would have only a few non-empty columns.  Therefore, it is useful to pre-merge the geofiles with the single summary level data files. This is precisely the format employed in the [Census Extract project](<https://github.com/CivicKnowledge/census-extract>), and similar to the way columns can be selected using the Census API.  Here is an example file in this format, for table B01001B, Sex By Age for Black or African-American Alone: [http://extracts.census.civicknowledge.com/2014/5/50_county/b01001b.csv ](<http://extracts.census.civicknowledge.com.s3.amazonaws.com/2014/5/50_county/b01001b.csv>) These files are also pre-linked with the geofile, using only the columns that are used for the county summary level, and the data includes both the estimates and the margins, so all of the information a user needs for analysis of the table is in a single file. 

### **Linkage Fields**

For at least the last 25 years, Census data files have had a set of linkage fields to connect records across multiple files. Like the sequence files themselves, these fields appear to be a legacy of distributing data on tapes but have now become an impediment.  In the latest ACS releases, these linkage fields are:

  * FILEID. File Identification
  * FILETYPE. File Type
  * STUSAB. State/U.S.-Abbreviation (USPS)
  * CHARITER. Character Iteration
  * SEQUENCE. Sequence Number
  * LOGRECNO. Logical Record Number

Of these fields, in the ACS releases, the FILETYPE, FILEID, STUSAB, CHARITER and SEQUENCE are constant for all rows in a sequence file, and most of them are constant across all files. Only LOGRECNO is required to link records in a single sequence file, and the combination of STUSAB and LOGRECNO uniquely identifies a record across the release.  Fortunately, the geoids, as they are formatted in ACS releases, have enough information to be unique across all records. So, it should be possible to eliminate the linkage fields on records and replace them with geoids. If use of these geoids were extended to data segment files, the geofile and TIGER geography files ( which currently use the old Decennial Census geoid format ) linkage across these multiple files would be much easier and less error prone.  ( One open question regards the CHARITER value, which is apparently unused in the ACS, but has been used in the Decennial Census. To use geoids for linking, it may be required to incorporate the CHARITER value in the geoid, or retain it in both the data and geo files. )

## **Normalize the Metadata**

The best form for releasing Census metadata is similar to the form already employed by the [Census Reporter](<https://censusreporter.org/>) project, which has [normalized all of the ACS releases from 2007 to 2014 ](<https://github.com/censusreporter/census-table-metadata>)into a common format.  This structure involves two data files, one for tables, and one for columns. Here are two examples of these files, in Google Spreadsheets: 

  * [Tables](<https://docs.google.com/spreadsheets/d/1CFowkTK0zsn-LBscwpEj0b-QmP_Y5B4wNnz9UhZywmw/edit?usp=sharing>)
  * [Columns](<https://docs.google.com/spreadsheets/d/1nBxHTwY4rypi5rhk4yOppQJD1vZzhjlF3_bo0j4NXq4/edit?usp=sharing>)

The improvements evident in these metadata files are: 

  * Separation of tables and columns make both of them easier to use.
  * The files are consistent and normalized. Data is not duplicated across multiple files. 
  * The columns file explicitly declares both the indent level for formatting columns and the ID of the column that each column rolls up to. 

The Census Reporter files are a nearly perfect form of table and column metadata, so they are frequently used in preference to the Census files for bulk importing Census data; both Civic Knowledge and CartoDB use these files in their projects.  One important addition to the metadata would be to document the parent/child relationship between columns, representing which columns are expected to sum up to a higher level column. This information is currently only encoded in the indentation in the excel metadata files, and can only be extracted by reading Excel formatting information. It should be represented with a “Parent” column that names the column that a column rolls up to. 

## **Publish Data in CSV format**

While Excel files are convenient, for tabular data CSV formats are much more portable and much easier to use programmatically. The first row of every CSV file should be a column header, holding the names of the columns.  Programmatic APIs should also allow for fetching data in CSV format, since CSV is immediately importable into any statistical program or spreadsheet, 

## **Formally Document Column Values**

There are several column values that are not completely specified, or are specified in ways that cause problems with data import. Most significantly are the geoids, which are critical identifiers but are not formally documented, and FIPS codes, which have a leading zero that is not always imported.  Geoids, as they are used in the American Community Survey, are well-designed identifiers that correct the limitations of earlier geoid versions. They are easy to construct, unique, and easy to parse. However, they are almost completely undocumented. While there are [successful projects to reverse-engineer the format](<https://github.com/CivicKnowledge/geoid>), geoids should be formally documented to ensure that there are no inconsistencies in how they are interpreted and used.  The identifiers for states, counties and places — and also the components of geoids — are FIPS codes ( the codes are actually specified [with an INCITS standard](<http://www.nist.gov/itl/upload/FIPSCodesReplacementChart2012.pdf>), although the ACS documentation refers to them with their previous standard term of “FIPS” ) which are formally documented, but because they have a leading zero, can be difficult to import. ArcMap has a [well known problem](<http://up206a.yohman.com/arcmaps-data-import-nightmare-text-or-number/>) with removing the leading zero, as does Excel and other spreadsheets. Automatic conversion of these values to integers frequently results in failures to link tables.  For most uses, it would be easier if the codes that never have a alpha component were specified as numeric, allowing the leading zero to be removed. Unfortunately, it’s difficult to determine what the specification actually requires, because the INCITS specifications are not open, and most public descriptions of the codes use the terms “digits” or “numeric,” which would indicate the codes are numeric, but they are also always listed as being zero-padded to a fixed number of digits, which suggests they should be treated as alphanumeric values.  To improve interoperability, these codes should be definitively, publicly and prominently specified as either being “alphanumeric” and requiring the leading zero to be preserved, or “numeric” and allowing the leading zero to be removed. ( Defining them as numeric means that the codes can never include a non-numeric value, which may be a problem for future expansion. ) If the values are declared to be numeric, their widths must be specified, so they can properly be composed into geoids, although that information could be part of the specification for geoids.  The specific data type of these values should be included in the geofile data dictionary, such as the one on pages 13 and 14 of the [2014 Summary File Technical document](<https://www2.census.gov/programs-surveys/acs/summary_file/2014/documentation/tech_docs/2014_SummaryFile_Tech_Doc.pdf>). 

## **Review and Reconsider the use of Fractional Line Numbers**

Every developer who has extracted bulk data has tripped over the use of fractional line numbers in the metadata to indicate an intermediate table heading. The fundamental problem seems to be that the fractional line numbers are only used for display of tables, and describe actual columns, although they appear in the metadata as a column.  These intermediate headings will require additional analysis to determine how to represent them in the metadata. 

# Recommendations Summary

In these recommendations, we’ve addressed two use cases, bulk loading and single file access.  For bulk loading, the [Census Reporter Metadata](<https://github.com/censusreporter/census-table-metadata>) provides an excellent example of a metadata format that is tailored for bulk loading, and is, in fact, used for bulk loading in at least three projects. For single file access, use the [Census Extract project api](<https://github.com/CivicKnowledge/census-extract>) formats census data in precisely the format that analysts would construct themselves, saving hours of work. Together, these examples and the other recommendations listed above can significantly reduce the effort required to use Census data for many users.

# Notes

## **Bulk Data Access and API Wrappers**

[Official Census API](<http://www.census.gov/data/developers/data-sets.html>)s. The collection of official Census APIs covers a wide range of datasets, although with a limited number of geographies [Census Reporter](<https://censusreporter.org/>). The Census Reporter site offers a beautiful collection of geographic profiles, tables and data search features, [along with an API](<http://api.censusreporter.org/>).  [Census.ire.org](<http://census.ire.org/data/bulkdata.html>). Prior to the Census Reporter project, the Census Reporter team created a browser for the 2000 and 2010 Census releases, including bulk download for a selection of summary levels.  [Census Reporter Postgres Scripts](<https://github.com/censusreporter/census-postgres>). Census Reporter releases their code for downloading ACS data and loading it into postgres. The scripts allow for directly importing ACS sequence files.  [Census Extracts](<https://github.com/CivicKnowledge/census-extract>), a project sponsored by an Amazon AWS grant, converts ACS data into smaller, single summary level files and makes them available in S3.  [CitySDK](<https://github.com/uscensusbureau/citysdk>), a proxy built on top of three Census APIs (Geocoder, Tigerweb, Statistics) [Sunlight Labs](<https://github.com/sunlightlabs/census>), A simple wrapper for the United States Census Bureau's API. [Koop](<https://github.com/koopjs/koop-acs>), and Open Source geospatial ETL engine, has an ACS adapter.  [CensusIQ](<http://arcgis.github.io/CensusIQ/>), a census search implemented using ESRI’s online tools. [ESRI’s Open Data service](<http://opendata.arcgis.com/datasets/06ab12f5dcaa40839729fbe49c298700_62>) entry for the ACS.  A [PythonToolkit](<https://github.com/RowanGeolab/ArcGISCensusDownload>) Bulk Downloader for ArcGIS. An [API Wrapper](<https://github.com/hrecht/censusapi>) for R.

## **Thanks**

Joe Germuska, [joe@germuska.com](<mailto:joe@germuska.com>), Knight Lab, Census Reporter  Ian Dees, [ian.dees@gmail.com](<mailto:ian.dees@gmail.com>), Census Reporter.  Jed Sundwall, Amazon Web Services Open Data
