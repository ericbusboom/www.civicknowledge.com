---
title: "Where San Diego Parties"
date: 2021-02-23T21:09:16+00:00
draft: false
categories: ["Mobility"]
author: "eric"
description: "Analsis of pedestrian traffic in downtown San Diego, comparing party time to work time."
---

San Diego’s CityIQ system – the 4,400 smart street lamps installed across the city – yields detailed data about pedestrian movements. We’ve condensed a few hundred gigabytes of observations of pedestrians from August 2018 to June 2019 [into a dataset of about 31M records](<https://data.sandiegodata.org/dataset/cityiq-io-pedestrians-san-diego/>), with the counts of the number of people walking in 2,600 walkways. I’d[ analyzed an earlier dataset to expose daily patterns of pedestrian traffic](<https://insights.civicknowledge.com/2019/04/pedestrians-rhythms-by-neigborhood/>), and now, with a more complete dataset, I’m exploring other topics. The latest is a look at the streets where San Diego parties and works downtown.

In this map, each street is colored according to the difference between the hourly rates of pedestrian traffic for work times ( weekdays, 6am to 5pm) and party times ( Friday and Saturday, 5PM to Midnight. ) Purple marks streets where there is much more work time pedestrian traffic, and green marks higher traffic areas for party time.

[![](/uploads/12/2019/06/Party-Map-Annotated.png?resize=960%2C774)](</uploads/12/2019/06/Party-Map-Annotated.png>)

Despite all of the businesses Downtown, most of the areas get more party traffic, with a few notable exceptions. In  the area marked “A”, the one work street is the site of a weekday Farmer’s market; the surrounding party area is the entertainment core of Little Italy. The Area marked “B” is the downtown Police headquarters. The areas “C” and “D” are residential areas; it isn’t clear why they are work hour hot spots.

For the very curious, the metric here is computed by taking the maximum count of pedestrians on any walkway per street segment per 15 minute interval, then grouping the observations into party times of the week  vs work times of the week and dividing by the number of hours in the party or work periods. This gives the max hourly rate of pedestrian traffic for Work times (W) and Party times (P). Then the metric is computed as (W-P) / ( W+P).
