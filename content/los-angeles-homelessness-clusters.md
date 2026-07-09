---
title: "Los Angeles Homelessness Clusters"
date: 2021-02-23T21:05:23+00:00
draft: false
categories: ["Homelessness"]
author: "eric"
description: "Maps of homelessness data from Los Angeles."
---

The Los Angeles County Economic Roundtable maintains a [data collection for the Los Angeles Point In Time homelessness counts](<https://economicrt.org/publication/los-angeles-county-homeless-count-data-library/>), as well as data sets for the associated in person surveys. It’s a really remarkable collection, with information both about the locations of the homeless, as well as information about their demographics and health issues. The [San Diego Regional Data Library](<http://sandiegodata.org>) has produced an [analysis dataset of the survey data](<https://data.sandiegodata.org/dataset/economicrt-org-homeless_survey-2011e2017>) with a few re-coded variables, including Census geoids, that make analysis easier.

For this example, we will link the survey responses to Census tracts and create a choropleth map colored by the race/ethnicity with the most people of that race/ethnicity surveyed in the tract. Note that this measure is only related to the most common race/ethnicity of the homeless of that tract if the surveyors interviewed people randomly. It’s possible that the interviews focused on a particular demographic, which would skew these results.

![](/uploads/15/2019/01/23036410-c3f8-4f70-81c9-b0387b887240-output_2_0.png)

Although it is possible that the interviewing was not a random sample, there is evidence that it probably is: the primary cluster of black-predominant responses corresponds with the tracts that have a high portion of Black population. The following map shows the protion of the total tract population that is black, for tracts with more than 10% of the population being black.

![](/uploads/15/2019/01/23036410-c3f8-4f70-81c9-b0387b887240-output_4_0.png)

### Share this:
