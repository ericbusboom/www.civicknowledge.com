---
title: "30 Million San Diego Parking Records"
date: 2021-02-23T21:10:19+00:00
draft: false
categories: ["Mobility"]
author: "eric"
description: "Temporal analysis of 30 million parking records from San Diego's smart streetlamp system."
---

San Diego has the[ world’s largest municipal Internet-of-things deployment, ](<https://www.currentbyge.com/cities>) which I got access to recently and have been pulling data from. I’ve now got about 30 million parking records — events when a car enters or leaves a parking zone — and have been processing and analyzing the data for the last few weeks.

The raw data is a bit difficult to use, because there are a lot of spurious events, but it isn’t hard to clean them out. The result is records, at 15 minute intervals, of the number of cars parked in each of the 6,600 parking zones across the city. Here are the two processed datasets.

  * [Parking Time Series](<https://data.sandiegodata.org/dataset/sandiego-gov-cityiq_parking>).  Parking events cleaned and aggregated to 15 minute intervals from Sept 2018 to Feb 2019.
  * [Location and Assets](<https://data.sandiegodata.org/dataset/sandiego-gov-cityiq_objects>). Metadata for parking zones ( and other objects ) including geo position, neighborhood and census tract.


These data were scraped [using my python module, cityiq](<https://pypi.org/project/cityiq/>).

I’m just starting to analyze the parking data ( and still scraping pedestrian events ) but have some initial analysis. Here is a rhythm map ( temporal heatmap ) showing the total flow, in or out, of all parking zones in Downtown, from September 2018 to Feb 2019, at 15 minute intervals through the day.

[![](/uploads/12/2019/02/tod-parking.png?resize=731%2C403)](</uploads/12/2019/02/tod-parking.png>)Downtown Parking Flow, By Month and Time of Day

There are some really interesting patterns here:

  * Strong inflow from 8:30 to 9:30 in the morning, which is expected.
  * Another strong inflow starting around 2:00PM, but varying by month.
  * The strongest outflow is around 1:00AM


It appears that last call is a stronger motivator to go home than quitting time.  Oddly, this pattern does not change much when aggregated by time of day.

[![](/uploads/12/2019/02/dow-parking.png?resize=677%2C403)](</uploads/12/2019/02/dow-parking.png>)Downtown Parking FLow, by Time of Day and Day of Week

I’ll be posting example Notebooks for how to use the datasets, and[ watch our Meetup](<https://www.meetup.com/San-Diego-Regional-Data-Library/>) for meetings about the datasets.
