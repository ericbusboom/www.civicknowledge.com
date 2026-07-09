---
title: "Public Data in California: Successes and Opportunities"
date: 2016-07-14T16:47:40+00:00
draft: false
author: "eric"
---

_California public data is excellent, but can be improved to make it more useful for a new generation of less sophisticated analysts and programmers by improving the structure of data packages and creating new aggregations of microdata._ California's state agencies produce a wide variety of high-quality data that are crucial for understanding important social issues in health, education, and government. While these data releases are generally excellent--in some cases the best in the US--there are also opportunities to make them even more useful and valuable. This document collects Civic Knowledge's recent experience with using datasets from the California Department of Public Health, the California Office of Statewide Health Planning and Development, and the California Department of Education to develop indicator websites and perform basic visualizations and analysis.  The viewpoints in this document are from the perspective of the mid-level analyst using open source software and spreadsheet programs to perform a range of broad data tasks, rather than more sophisticated users, such as an epidemiologist who uses dedicated statistical packages like SAS. This perspective is particularly valuable as agencies in the state of California expand their data programs, because it is precisely the mid-level of data skill that represents the largest set of new users. So these recommendations are intended to ensure that California’s high-quality data releases are just as valuable and usable for the new set of users as they have been for the more experienced analysts that form the traditional base. These recommendations are organized into two areas: 

  * **Data packages.** Civic Knowledge recommends maintaining and emphasizing the package-oriented organization of datasets while transitioning to Socrata data repositories. It further recommends developing standards for how data should be packaged.


  * ****Creating public aggregations of private data.** Many valuable datasets are hard to acquire due to privacy restrictions, but could be published in aggregated form, using the American Community Survey as a model.**

These recommendations are solutions to common problems that make data projects more difficult, particularly projects that use data from multiple sources. Some of these issues include: 

  * Data repository software emphasizes files, not data packages, so it is difficult to understand the scope of a large collection of files and find appropriate documentation. 
  * Data dictionaries are the first and most important documentation for a dataset, but they are sometimes hard to find. When using data in a program, data dictionaries must be loaded into the program, which is very difficult to do when a data dictionary is in PDF format. 
  * When a dataset has dimensions that refer to common entities, such as geographic areas, users will want to link them. Many datasets that refer to geography have, for instance, a county name, which is much more difficult to link than a Census geoid. 
  * Datasets inconsistently present important values such as confidence intervals, standard errors, and rate denominators.
  * Many valuable datasets are hard to acquire because of privacy restrictions, even though the end-users really need de-identified, aggregate data. 
  * Many aggregated datasets are based on small samples, so they can’t be analyzed on other dimensions, like race or social class. 

Fortunately, these problems have fairly easy solutions, which are described in this document. 

# Working with the Public

Development of these recommendations should involve the public, specifically, input from organizational data users. Some of the organizations that could provide additional input are: 

  * Nonprofits
    * Public Policy Institute of California
    * Public Health Institute
    * California Common Sense / US Common Sense
    * Investigative Reporters and Editors (IRE) 
    * California Endowment
    * Strategic Growth Council (SGC)
    * Bayes Impact
  * Government
    * County Health Departments, Epidemiologists

While a specific outreach program would require more design, it should probably begin with a series of one-on-one interviews to establish a baseline draft, followed by a series of online working meetings to refine the recommendations. 

# Data Packaging Recommendations

Virtually all of the most valuable datasets are complex, with multiple files, data dictionaries, and documentation. Typically, these separate assets are combined into a package that links the files together through a web page or by inclusion in a single ZIP file.  Data repository software often has a file orientation, which makes file operations much easier, but which can obscure the relationships between files in a package. While transitioning to data repositories, agencies should ensure that the package structure they have established for critical datasets are maintained. 

# Successes

In general, the way California agencies package and release complex datasets is excellent, with the substantial effort required to address important details being clearly evident. In fact, nearly all of the recommendations in this section are based on observing existing packages, so while there are opportunities for improvement, they are better described as possibilities to make the successes more pervasive. 

# Opportunities

While preserving packages is important, there are also opportunities for improving data packages by defining some guidelines for how packages are organized and described. Some of these recommendations are: 

  * **Standardize the structure of packages.** Create standards for the structure of data packages, including data dictionaries, documentation, and file formats.
  * **Formalize entities.** Formalize datasets about entities, such as the OSHPD Facility crosswalk file, or the CDE school and district entities. 
  * **Formalize common dimensions.** Formalize common dimensions, such as age, race/ethnicity, income, and poverty status. When available, reuse existing standards, such as census geoids. 
  * **Use standard codes and distinguish from labels.** Names of things, like a county name or a school name, are hard to link. When a name is used in a dataset, it should always be associated with a well-known code
  * **Create standards for column names.** Create standards for column names and column name prefixes, such as the suffix “_pct” for percentages.

 

# Organize Data as Packages

_Organize and present datasets as cohesive packages, rather than individual files._ The most valuable data published by state agencies are organized as related collections of files and documentation. This organization should be emphasized and formalized as cohesive data packages. Currently, nearly all of the most valuable data are organized this way, but the benefits of this organization should not be forgotten as agencies expand their data publication programs using Socrata data repositories. Open Data Portals, such as Socrata or CKAN, provide agencies with an easy way to publish data, encouraging them to release more data to the public. They do, however, have some disadvantages compared to publishing data to an agency’s website.  From a data user’s perspective, data repositories are most oriented toward serving individual files, while the most valuable datasets are cohesive collections of files, and these datasets are much harder to use when they are disaggregated.  One such complex dataset is the CDPH Healthy Communities Index (HCI), a collection of 21 indicators for community factors and health disparities. The collection is one of the state’s most useful data products, because it presents many indicators from different sources in a common format, indexed to common geographies, making it much easier to use than the raw sources. The collection is very well documented, is updated regularly, and has a good web page, which links to all of the files.  The main page for the HCI is easy to find with a [Google search for “California Health Community Indicators.”](<https://www.cdph.ca.gov/programs/pages/healthycommunityindicators.aspx>) The page is designed for other data users by a skilled analyst, presenting the goals of the project, primary documentation, a list of individual files, documentation for individual files, and support code for specific statistical packages. This page, despite its informal web design and an occasional broken link, is a perfect example of how to present information to a data user.  Now compare that page to the[ search results for “Health Community Indicators” ](<https://chhs.data.ca.gov/browse?q=Healthy%20Communities%20Indicators&sortBy=relevance&utf8=%E2%9C%93>)on the CDPH Open Data portal. The visual design of the page is far better, but rather than presenting the dataset, this is a search page for the individual files in the dataset, with none of the context provided by the HCI web page. [Clicking through to one of the search results](<https://chhs.data.ca.gov/Demographics/Unemployment-2004-2013/u729-zehn>) presents a tabular view of the data, again without any of the context. However, for an analyst in the early stage of evaluating data for a project, the data dictionary and other documentation are much more important than the data, and should be presented more prominently than the data.  Because the documentation links for the HCI files are critical for properly using the HCI files, an analyst who is using the HCI via the Open Data portal will have to locate the “About” link on the repository page and click through to the primary HCI web page. This is a much more cumbersome process that just looking for the HCI dataset in Google.  However, the Open Data portal does have some advantages over the main HCI web pages, such as providing a consistent interface to downloading data, allowing data download in a variety of formats, and providing an API to the data. There are substantial benefits to be gained by combining the best features of a dataset web page with a repository like the Open Data portal. 

## **Successes**

Individually, both the HCI web page and the Open Data portal have important benefits. The HCI web page is a first-rank resource for understanding and using the HCI indicator dataset. It is well organized, easy to read, and remarkably thorough. The data portal version of the HCI web page offers a consistent download interface, a variety of download formats, and an API. By coordinating the repository with the web page, their advantages can support each other. 

## **Opportunities**

Because each of the presentations of the HCI data has unique advantages, it would be very beneficial for them to be combined, with an inversion of the links between them: the files should be stored primarily in the Open Data portal repository, and the HCI web page should link to the files in the data repository. In this model, there would be a normal web page for each complex dataset, which would be the entry point for accessing files stored in the data portal repository. Additionally, the search results in the data portal repository should link to the main webpage for a dataset. For instance, a user searching for “Healthy Communities” in the CHHS Open Data repository should get a link to the main HCI webpage, and from that webpage would access the individual files.  Organizing the files in this manner would prevent users from having to choose between the web page and the data portal repository, and each would focus on their unique advantages. 

# Standardize the Structure of Packages

_Datasets should have a consistent format, including documentation, data dictionaries, and files._ Because the most valuable datasets are collections of data files and documentation, and because datasets should be presented as packages, it is also valuable to provide dataset creators with guidance on how to organize datasets. A consistent organization makes it easier for creators to ensure that their packages meet the needs of data users, and easier for dataset users to transfer knowledge about one dataset to others.  While a standard for the organization of data packages can be arbitrarily complex, there are a few basic principles that will ensure that the data package is suitable to the widest range of users: 

  * Datafiles should be formatted as CSV, rather than fixed-width, tab-delimited, or Excel. SAS and SPSS should be accommodated with PROC files to read the CSV formatted data. 
  * Documentation files should be PDF or HTML, not Word.
  * Data dictionaries should be CSV files, although the same information may appear as a table in the main documentation.
  * Data should be packaged using a ZIP file, with the files within a subdirectory in the archive. The subdirectory should have the same name as the ZIP file, excluding the .zip extension. 
  * Separate files should be included for detailed information about entities, such as schools or hospitals. 

CSV files are important because not only can they be opened in any spreadsheet program, they are also easy to use from any programming language.  Encoding data dictionaries in CSV files is another important way to ensure data can be easily used in multiple environments. It is fairly common for users to load data into a database, which requires creation of a schema. Creating database schemas, or other similar transformations of metadata, is much easier when the data dictionary is machine readable.  When a data file has rows that represent a complex, non-standard entity, such as a school or a hospital, the package should include an entities file with more complete information about the entity. Files that address standard entities, such as counties or states, do not require an entities file, but may include one as a convenience.  When there are multiple files, they should be collected in a ZIP file. The file has one top-level directory with the same name as the ZIP file without the .zip extension. 

# Formalize Entities and Use Codes and Labels

_Define well-known names and ID numbers for schools, hospitals, and other entities, and link together the entity code and its text label._ Entities are the things that data is about. Some common entities in public datasets are: 

  * Geographic areas
  * Schools
  * Hospitals
  * People
  * Businesses

Many of these entities have identities assigned to them by a central authority. Geographic areas are defined and numbered by the US Census Department, California schools have CDS numbers, and businesses have ID numbers assigned by the California Secretary of State. When these entities appear in a dataset, they should always be primarily identified by their most authoritative ID number, and secondly by their common name.  The codes are important because text names are very difficult to link. There can be many variations of a name, and when they are entered by a person, they may have errors and omissions. Consider two hospital files describing the same hospitals, one with “Fifth Street Emergency” and another with “5th St. Emergency”. These names are nearly impossible to link automatically, but both of these hospital entries should have exactly the same administrative code.  However, while the codes are linkable, they are difficult for humans to understand, so datasets with all of the entities represented only by codes are difficult to analyze.  To address both of these problems, entities that have administrative identifiers--people, schools, counties, etc--should always be identified by their well-known code, with a “label”-- the name of the entity--associated with the code. To enforce the link between the two, the column with the label should have the same name as the code column (or the root of the name of the code column) with a “_label” prefix.  For instance, an example of column names and row contents might be:  **county_geoid** | **county_geoid_label**  
---|---  
05000US06003 | Alpine County, California  
05000US06005 | Amador County, California  
05000US06007 | Butte County, California  
05000US06009 | Calaveras County, California  
05000US06011 | Colusa County, California  
05000US06013 | Contra Costa County, California  
05000US06015 | Del Norte County, California  
  In large datasets that have dimensions of limited cardinality--such as a “race” dimension with 7 different values--the labels may be external to the dataset, but should be included in a data file that can be machine-read. For instance, a survey may have answers given in a Likert scale (1 to 5), with labels that differ for each question. For one question, a “1” may mean “Yes, I would definitely buy this product again.” To reduce the size of the file, these labels could be included in a separate CSV file (prefered for programmers) or in a file of SAS, Stat, or SPSS label commands.  However, if including the labels would not make the file unmanageably large, they should be included in the file. This is particularly true for geographic names, age groups, or race-ethnicity codes. Including the labels makes it easier to interpret analysis results and to create charts with the correct axis labels.  When a file has geographic entities that are defined by the US Census, always use the ACS-style geoids to reference Census geographies. There are three geoid styles, one for the decennial Censes, one for the annual American Community Survey, and one for the TIGER geographic files. The ACS version includes extra values (the summary level and geo component) that make them unambiguous, whereas, for the other two, different areas can have the same code. Always use the ACS geoid to reference geographic entities that are defined by the Census.  On the other hand, it is frequently valuable to have other codes for geographic areas, particularly when the geographic entities are entirely within California, although using these codes can make linking difficult. For instance, the most common codes for counties are FIPS county codes, which have leading zeros when they are represented as strings. For example, Amador County may be represented as “005,” “05,” “5,” or 5.  This problem can be solved by always representing the codes with an integer datatype, which will remove the leading zeros, but this should only be done when the definition of the code does not allow for character codes.

# Formalize Common Dimensions

_For common dimensions such as race, ethnicity, or age, use a single, common definition of the dimension._ Dimensions are independent values that, taken together, identify a measurement. In social data, dimensions are usually either time or a property of the entity being measured. Some common dimensions in social data are: 

  * Time
  * Geographic area
  * Age
  * Race/ethnicity
  * Sex
  * Income
  * Federal poverty status
  * Marital status

Generally, rows in datasets can only be linked or compared along dimensions when the dimensions have the same range of values, and each of the values has the same definition. For instance, a dataset that has a racial definition of “White” that includes Hispanics is difficult to compare to a dataset where the definition of “White” includes only non-Hispanics. Defining dimensions so they can be used across many datasets makes combining data from multiple sources much easier.  For most of these demographic dimensions, the best option is to define the dimension to match the Census and American Community Survey, which has useful definitions for race, ethnicity, age groups, income groups, and other factors.  When including dimensions in a file, consider inserting both a code and a label. For instance, these race/ethnicity codes are harmonized with the American Community Survey: raceeth | raceeth_label  
---|---  
aian | American Indian and Alaska Native Alone  
asian | Asian Alone  
black | Black or African American Alone  
hisp | Hispanic or Latino  
nhopi | Native Hawaiian and Other Pacific Islander Alone  
white | White Alone  
whitenh | White Alone, Not Hispanic or Latino  
multiple | Multiple  
other | Some Other Race Alone  
all | Total Population  
  
# Create Standards for Column Names

_A consistent form for column names make it easier to understand datasets._ When using a dataset, it is important to know what kind of data each of the columns hold, and having standardized names can make using and joining datasets much easier. Because there is a nearly infinite variety of names for data columns, it’s actually suffixes for the column names that should be standardized, while the main column names should follow a few rules.  Column names should be usable without alteration in all spreadsheet programs, statistical packages, and programming languages. To ensure compatibility with many different environments, columns should be composed entirely of lowercase letters, numbers, and the underscore (“_”) to separate words. Additionally, the first character of the name must not be a number, and only columns with special meaning should start with an underscore. **Good Names** | **Bad Names**  
---|---  
county_poverty_rate | County Poverty Rate  
county_rate_1 | 1st_county_rate  
  For an example of a suffix, if a dataset has a count of impoverished households in a column named “poverty,” it may have the percent of households in poverty in a column named “poverty_pct.” Standardizing these suffixes make datasets much easier to understand and use.  These suffixes serve two purposes: to document what kind of value a column holds, and to link columns together. In the example below, the first column is a poverty count, and all subsequent columns are related to the poverty count. If the meaning of the prefixes is well understood--such as “_pct” is always a percentage in the range of 0 to 100--then the column can be fully understood without reading the data dictionary.  Here is an example of a possible naming scheme.  **Column Name** | **Description**  
---|---  
poverty | Count of households in a geographic area with an income below the poverty level   
poverty_rate | Number of households below the poverty line per 100,000 households  
poverty_pct | Percentage of households below the poverty line  
poverty_m90 | 90% margin for the poverty count  
poverty_ci90l poverty_ci90u | Lower and upper 90% confidence intervals for the poverty count  
poverty_se | Standard error in the poverty count  
poverty_rse | Relative standard error of the poverty county  
poverty_pct_se | Standard error of the poverty_pct  
 

# Aggregating Restricted Data

Some of the most valuable datasets in California are also the most difficult to use. Datasets such as the Death Statistical Master Files, Patient Discharge Data, and the Linked Births files are important for many research and indicator projects, but anyone who wants to use this data must meet significant requirements due to privacy restrictions.  However, many of the prospective users of these files do not need the individual-level records and would immediately aggregate the files to geographic areas, age groups, or racial groups. If state agencies created these aggregates, the files could be publically distributed, resulting in wider use of these critical datasets. Here are some recommendations: 

  * **Develop aggregates of birth, death, and hospital data**. These files are very valuable but are difficult to acquire and use. Aggregated versions would increase the data value significantly. 
  * **Consider non-geographic aggregates**. Geographic aggregation is most frequently requested, but subdivision by race or other demographic factors increases errors. Consider releasing files with alternate primary aggregations. 


# Develop Aggregates of Birth, Death, and Hospital Data 

A good model for the design of the aggregates is the American Community Survey, which takes surveys of about 7% of the US population and produces a dataset of 330 subject tables, with some survey questions resulting in a dozen tables. While the results are always aggregated to geographic dimensions, different tables will have a variety of secondary aggregation dimensions, such as sex, age group, or poverty status.  A similar aggregation model could produce from the California Death Statistical Master Files a collection of aggregations that could be publically available, each tuned to specific data use. One such aggregation is the [3-4-50 Deaths file from San Diego County](<https://data.livewellsd.org/Non-Communicable-Chronic-Disease/Trended-3-4-50-Chronic-Disease/kpde-gmvn>). 

# Create Multi-Year Aggregates

Data users usually want the smallest aggregation areas possible, but most datasets have too few records to produce stable estimates for areas smaller than counties. By aggregating multiple years, as the American Community Survey does with its 5-year release, datasets can address smaller geographic areas

# Geographic Components

When the typical sub-county aggregates are not stable, an alternative sub-county aggregation strategy is to use Census geographic components, which aggregate smaller regions in a region based on physical or demographic characteristics of the smaller area. The resulting aggregation areas are not contiguous, but have analytical value when they align with known explanatory factors.  For instance, deaths could be reported per-county, and within each county, by whether the zip code of the person’s death was rural or urban. Other factors, such as median household income, average age, or percentage of home ownership, would allow for the public release of datasets that address important analytical questions without compromising privacy. 

# Non-Geographic Aggregates

There are two primary reasons for aggregating to geography: the data user wants to restrict the data question to a particular political boundary, or the user wants to link the results to Census data. The first case requires a geographic aggregation, but the second could be handled by directly aggregating on the same dimension that the user wants to link on. For instance, the dataset could be aggregated on race/ethnicity, age group, or family income. 

# Correlates, Odds Ratios, and Risk Ratios

Another significant use for many microdata files is to produce correlates, odds ratios, or risk ratios. It may be valuable to release datasets of the parameters used to calculate odds and risk ratios for selected pairs of variables.
