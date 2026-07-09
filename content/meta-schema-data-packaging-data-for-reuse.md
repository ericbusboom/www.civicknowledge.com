---
title: "Meta, Schema, Data: Packaging Data For Reuse"
date: 2016-06-09T20:09:26+00:00
draft: false
author: "eric"
---

_Public data can be much more useful with small improvements to how it is documented and packaged._ Despite decades of enthusiasm for data, it is still difficult and expensive to distribute data from producers to consumers. Skilled data analysts have access to more data than ever, but the broader range of data users, such as journalists, nonprofits, businesses and consumers still have difficulty finding and using data. Websites such as Census Reporter and DataUSA.io offer a model for how to increase data use, but these types of sites are very expensive to poduce.  To solve these problems, we propose a way of packaging data that can make data distribution sites like Census Reporter much easier to create and maintain, and ensure traditional analysts can find the data they need. These method add some cost to the data production process, but will yield enormous benefits to data consumers.  By developing simple standards for how to package data, data producers can make their datasets “machine comprehensible,” permitting the creation of better data access software that can store, publish, and visualize any properly packaged dataset. Better data packaging will result in making data:

  * Easier to find, because the packages can be indexed in search engines.
  * Easier to view, because software can automatically create charts.
  * Easier to analyze, because the files will reliably load into statistical software
  * Easier to publish, because there are fewer decisions for data publishers to make. 

The standards we propose are very simple. For the most part, it simply involves adding to a data package a single Excel file, with two additional worksheets. One worksheet has the title, author, publication date of other dataset, and the other has a description of each column in the datatable. The data can be included as a third worksheet, making a properly constructed data package into a single Excel file. 

# What Is It Good For?

A well defined, documented, complete and consistent data package format is valuable for both producers and consumers, humans and computers. 

  * Data analysis will get get all of the information they need to use a dataset.
  * Programs can read the schema and metadata to do automatic processing.
  * Data producers can create high-quality data packages with fewer decisions.

The most exciting benefit is automatic processing. Some of the ways that data packages can be automatically processed include: 

  * **Generate web pages**. Software can read one or more packages to create entire data repository websites, based entirely on the data package, with no additional input. 
  * **Improved search engine indexing**. When generating a webpage, the webpage can be design to make the dataset easy to find, which is currently difficult when the metadata and data dictionary are in different files. 
  * **Automatic visualization**. Visualization programs can use the metadata to infer the most important charts and graph, and create them automatically. 
  * **Automatically import metadata into Socrata**. With a Socrata plugin, Socrata could automatically import metadata from the package file. 


# Why is Data Use Hard

Expert data users are adept at finding datasets in Google, downloading files and importing them into data analysis tools like SAS, R or a SQL Database, but these tools and processes are outside the skill set of most people who want to use data. Most users will get data from data access websites ( such as [Health Indicator Warehouse](<http://www.healthindicators.gov/>) ) or indicator websites ( such as [Kids Data](<http://www.kidsdata.org/>) ) which condense datasets into facts or provide data search and download features. But because of high costs, there are relatively few excellent data access websites. Census Reporter, for instance, cost about $500,000, and costs of $250,000 or more are typical. A high quality indicator website can cost $5,000 per indicator for just the data management, and several hundred thousand dollars more for the website.  Data management is expensive because of the variety of data files, structure and quality, and these costs could be greatly reduced if the process of ingesting data into a web site could be automated. Automated ingestion can only be accomplished if data releases are packaged with machine readable metadata that describes the dataset sufficiently to understand and manipulate the data programmatically.  If datasets could be manipulated programmatically, it would be possible to treat data as packages -- like phone apps or desktop programs -- that could be installed into indicator software, making possible a variety of commercial and Open Source indicator programs that could use any properly packaged dataset. So, if we want to make data more accessible and useful, we need to have better metadata, and linking that metadata to the data involves data packaging. 

# An Example Package

Suppose we want to publish this data table:  **time** | **color** | **color name** | **shape** | **weight** | **temperature**  
---|---|---|---|---|---  
4 | 1 | red | circle | 4 | 27  
10 | 2 | blue | square | 6 | 29  
17 | 1 | red | triangle | 3 | 30  
23 | 3 | yellow | square | 2 | 25  
In a single Excel-file package, this table might be put in a worksheet named “data.”  The core metadata for the package is stored in the second worksheet, named “meta.” Here is an example of that worksheet:  **property** | **value**  
---|---  
Title | An Example Data Packages  
Description | This data package is an example of how simple a data package can be  
Subject | Examples of data packages  
Creator | Eric Busboom <eric@civicknowledge.com>  
Publisher | [http://www.civicknowledge.com](<http://www.civicknowledge.com>)  
The final worksheet is named “schema,” and it holds a description of the data:  **Column** | **Role** | **Datatype** | **Description**  
---|---|---|---  
time | dimension | time/second | Time at which the part was sampled, in seconds from the start of the experiment.  
color | dimension | color/int | Color code number.  
color name | label | label(color) | Crayola name for the most similar color.  
shape | dimension | string | Shape category, circle, square, or triangle.  
weight | measure | weight/gram | Weight of part in grams.  
temperature | measure | temp/c | Temperature of part when it was sampled, in Celsius.  
The “schema” worksheet is a traditional “data dictionary” document, but it has more detail in the Datatype column. The names of the data types in the Datatype column is the most detailed part of the specification, but for now, it is only important to know that the names in this column describe what the data in the column is for and what it does, rather than just whether it is text or a number.  This example is [implemented as an Excel file](<https://civicknowledge.box.com/shared/static/qdja090081dwphdckzedaunleox88jv9.xlsx>), but many other forms are possible, such as a [Google Spreadsheet](<https://docs.google.com/spreadsheets/d/1wuqwgjVsZbT5Vs_EXvBgWD5kzkQR4dJr19RjsGqtJys/edit?usp=sharing>), three [CSV files in a ZIP archive](<https://civicknowledge.box.com/shared/static/3n452602avp5csy2hqy1m0qc7cz87d7o.zip>), and other structures when there is more than one datafile in a package. However, all of the forms follow the simple model shown above. 

# Next Steps

We are currently working on [a more detailed specification](<https://docs.google.com/document/d/1eZRjI4Cv1jdfrelj0Il-n2vrdYzp6U4WMleG0O6xdp8/edit?usp=sharing>), which will provide a formal definition of the package structure and how to create them. Meanwhile, we are also recruiting interest from data users and data producers to talk about requirements and develop a draft specification. If you are interested in participating in this project, please contact Eric Busboom at [eric@civicknowledge.com](<mailto:eric@civicknowledge.com>).__
