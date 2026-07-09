---
title: "View from Streetlamps: San Diegans are Staying Home"
date: 2021-02-23T15:19:13+00:00
draft: false
categories: ["Mobility"]
author: "eric"
description: "Visualizations of pedestrian traffic in San Diego showing the impact of COVID-19 lock down orders."
---

_Pedestrian counts from[San Diego’s smart streetlamps](<https://www.sandiego.gov/sustainability/energy-and-water-efficiency/programs-projects/smart-city>) indicate that San Diegans responded strongly to stay at home orders, but the data has some weaknesses, and the reduction has several causes._

In 2018, [San Diego installed over 4,000 smart street lamps](<https://www.sandiego.gov/sustainability/energy-and-water-efficiency/programs-projects/smart-city>), one of the largest deployments of the CityIQ system in the world. These Internet-connected street lights give developers access to data on the intensity of pedestrians and traffic. But not anyone’s identity — the data is completely anonymous.

The Data Library has been analyzing this data for over a year, to examine [daily rhythms in pedestrian traffic](<https://insights.civicknowledge.com/2019/04/pedestrians-rhythms-by-neigborhood/>), hourly [patterns in downtown parking](<https://www.sandiegodata.org/2019/02/30-million-san-diego-parking-records/>), and insights into [where San Diego goes to party](<https://www.sandiegodata.org/2019/06/where-san-diego-parties/>). We can use this same data source to visualize how well San Diegans have responded to heath department orders to stay home. Here is a plot of the pedestrian traffic from a set of about 12 sensors, in multiple neighborhoods around San Diego, including dates for storms ( blue ) and two closure orders (red), one for San Diego Unified School District, and one issued by the Mayor’s office of the City of San Diego.

![](/uploads/19/2020/04/Screen-Shot-2020-04-21-at-9.59.18-AM.png?fit=1024%2C572&ssl=1)

Note that the Y axis is unitless — traffic is expressed relative to the highest count for the year, because there is a lot of change in how many sensors are online and reporting, so only a relative measure makes sense. This plot makes it very clear that there is much less pedestrian traffic than normal, but it is not clear that the reduction is directly associated with the orders. The storms may have had an effect of driving traffic down, and the orders kept it down, but maybe there are other factors.

One possible other factor is that people had been primed by other news avout COVID-19 to want to avoid being out in public. If so, this may show up in Google search traffic, which we can explore by looking for COVID-19 related terms in Google Trends. Here is what search traffic looks like for “COVID-19” and “coronavirus” 

trends.embed.renderExploreWidget("TIMESERIES", {"comparisonItem":[{"keyword":"covid-19","geo":"US","time":"2020-03-01 2020-04-01"},{"keyword":"coronavirus","geo":"US","time":"2020-03-01 2020-04-01"}],"category":0,"property":""}, {"exploreQuery":"date=2020-03-01%202020-04-01&geo=US&q=covid-19,coronavirus","guestPath":"https://trends.google.com:443/trends/embed/"}); 

Overlaying that on the pedestrian traffic plot, it does look like a there is a relationship:

![](/uploads/19/2020/04/Ped-vs-search.png?fit=1024%2C553&ssl=1)

But, that relationship would be easier to assess with a scatter plot, showing the regression line, and maybe a correlation coefficient.

![](/uploads/19/2020/04/ped-vs-search-scatter.png?fit=1024%2C583&ssl=1)

There clearly is a relationship there, but a correlation of -.52 isn’t very impressive. The correlation is a bit better if we look at just the period of when the pedestrian traffic is declining, from March 7 to March 18. In that range, the correlation is about 0.7.

While that correlation still isn’t decisive, it is using data that has a complex structure, and some hidden gotchas. The San Diego CityIQ system has about 4,400 nodes, not not all of these nodes report consistently, and lately, there has been a significant decline in the number of nodes that are reporting pedestrian traffic. Here is a plot of the number of walkways ( a virtual line in the sidewalk that the sensors detect when a person walks across ) that have at least one report per day, for all of the data in the system.

![](/uploads/19/2020/04/node-count.png?fit=1024%2C540&ssl=1)

Note that the plot has a log-scale Y axis, so the peak number of walkways is in the thousands, but the number for the last month has been about 10, with the total dropping to zero for a few days. This is a lot of variability in the number of online sensors, and it’s is tricky to analyze data where sensors’ availability is inconsistent. Fortunately, one of the most constant periods is also the period of time we are studying for this post, but longer term analysis can be very tricky.

Pedestrian traffic has clearly declined since the start of the COVID-19 crisis — we can see that everyday on the street, without data — but the use of data doesn’t give us a single, clear-cut answer about the cause of the decline. However, this is a typical result of data analysis, and a common fact of life: important changes can have many causes. In this case, I suspect that the story of why fewer San Diego are walking around starts with the weather and the news, and only ends with government health orders.
