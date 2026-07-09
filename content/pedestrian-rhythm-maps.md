---
title: "Pedestrian Rhythm Maps"
date: 2021-02-23T21:01:55+00:00
draft: false
categories: ["Mobility"]
author: "eric"
description: "Visualizations of pedestrian flow in San Diego."
---

_San Diego’s CityIQ system consists of about 4,400 smart street lamps, which use a variety of sensors to track parking, pedestrians, traffic and a variety of environmental conditions. This analysis reveals pedestrian paterns using time-oriented heatmaps._[ ](<https://github.com/sandiegodata-projects/insights.sandiegodata.org/blob/main/blog-notebooks/urban_planning/CityIqPedestrians.ipynb>)

This dataset aggregates the number of pedestrians, traveling in either direction, into 15 minute intervals, per walkway, and links the walkways to communities. Then, data is visualized by community in a heat map with two time dimensions, known as a rhythm map. Since this data is only available for the prior 6 months, we can’t analyze long term patterns, so we only present a few types of maps, including traffic for hour of day versus day of week and for hour of day versus week of year.

# Day of Week By Hour[¶](<https://insights.sandiegodata.org/2020/11/02/pedestrians-rhythms-by-neigborhood/#Day-of-Week-By-Hour>)

This sort of rhythm map shows intensity for hour of the day versus day of the week over the entire data period, revealing weekly patterns. For the community of Claremont Mesa, we see that most of the pedestrian traffic is in the weekday afternoons. Notice that traffic increases later in the day on the weekend.

![](/uploads/2020/11/403069d0-1f6f-47be-8fee-6f5552918510-output_6_0.png)

Mission Beach shows a different pattern, with more of the traffic on the weekend, or on Thursday.

![](/uploads/2020/11/403069d0-1f6f-47be-8fee-6f5552918510-output_8_0.png)

But the military facilities show a very different pattern, with nearly all activity in the early morning or evening.

![](/uploads/2020/11/403069d0-1f6f-47be-8fee-6f5552918510-output_10_0.png)

The Downtown area is one of the most interesting, because it has a lot of workers during the day, and a lot of residents, and the most active entertainment areas. All of these patterns can be seen in it’s rhythm map: a strong weekday noon line for workers going to lunch, an increase on Fridays and Saturday evenings and generally high traffic all of the time.

![](/uploads/2020/11/403069d0-1f6f-47be-8fee-6f5552918510-output_12_0.png)

# Date versus Hour[¶](<https://insights.sandiegodata.org/2020/11/02/pedestrians-rhythms-by-neigborhood/#Date-versus-Hour>)

Here is a longer term view, for Pacific Beach, showing traffic by hour for each week of the data. It shows that in Pacfici Beach at least, there is little seasonal variation in traffic patterns.

![](/uploads/2020/11/403069d0-1f6f-47be-8fee-6f5552918510-output_14_0.png)

# Line Plots[¶](<https://insights.sandiegodata.org/2020/11/02/pedestrians-rhythms-by-neigborhood/#Line-Plots>)

It’s a bit hard to tell the relative values of the colors, so here are some of the communities expressed in line charts, with traffic per hour over the whole dataset. The difference in morning to evening traffic can be a factor of 3 to 6.

![](/uploads/2020/11/403069d0-1f6f-47be-8fee-6f5552918510-output_17_0.png)
