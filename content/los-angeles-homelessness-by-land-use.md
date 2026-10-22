---
title: "Los Angeles Homelessness By Land Use"
date: 2021-02-23T21:04:45+00:00
draft: false
type: "post"
categories: ["Homelessness", "Project"]
author: "eric"
description: "How land use in Los Angeles is associated with homelessness."
---

_An exploration of the Los Angeles homelessness counts allocated to land use categories._[ Full notebook on github](<https://github.com/CivicKnowledge/insights.civicknowledge.com/blob/master/homelessness/Homelessness.ipynb>)

The Los Angeles Homeless Services Authority is responsible for conducting the annual Point-In-Time-Count of homeless people in Los Angeles, and publishes the data to their website. The dataqset they publish dataset is re-packaged for easier analysis at the [San Diego Regional Data Library’s Data Repository. ](<https://data.sandiegodata.org/dataset/lahsa-org-homeless_count-2018-los_angeles>). This analysis links the Data Library’s data package to LA City tax assessor’s parcels to study estimates of homless populations organized by land use categories.

# High Density Homelessness[¶](</los-angeles-homelessness-by-land-use/#High-Density-Homelessness>)

The PITC records counts for 2159 census tracts in Los Angeles county, but most have reatively few homeless. This map shows the top 50 tracts with the higest density of homeless. The yellow tract is Skid Row, the highest homeless density neighborhood in the state. Other tracts are Downtown, Venice, Stanta Monica, Van Nuys and other high density neighborhoods.

![](/uploads/4/2019/01/2c640a94-03b3-4dee-ac8b-8b17346c8227-output_9_0-1.png)

Homelessness is very concentrated; most of the homelss are in a small number of neighborhoods, although there are some variations in the distributions by the category of homelessness. The distributions for makeshift shelters and tents is narrower than that of the total unsheltered, meaning that people in structures and tents are more clustered togehter than those without stuctures or tents. This analysis will primarily use the total count of homeless, so note that for other categories, the distributions will be different.

![](/uploads/4/2019/01/2c640a94-03b3-4dee-ac8b-8b17346c8227-output_11_0-1.png)

The PITC ( point in time count ) in Los Angeles categorizes homeless as individuals or part of families, makes estimates of age, and records what kind of shelter the person or group may have, including cars, vans, campers, tents, makeshift structures, or offical, established shelters. For these counts, “Unsheltered” means the person is living in a place that is not meant for human habitation, which includes cars, campters, tents, RV and makeshift structures, although the counts for the number pf people living in enclosed spaces is usually an estimate. HUD [publishes a guide for counting the homeless](<https://www.hudexchange.info/onecpd/assets/File/Guide-for-Counting-Unsheltered-Homeless-Persons.pdf>) that explains the terms in more detail.

Most of the people counted in the LA homeless count are counted outside enclosed spaces, not in campers, vans, tents or structures — the ‘total’ count is much larger than the categories for enclosed spaces.

![](/uploads/4/2019/01/2c640a94-03b3-4dee-ac8b-8b17346c8227-output_13_0-1.png)

# Homelessness by Land Use[¶](</los-angeles-homelessness-by-land-use/#Homelessness-by-Land-Use>)

The LA PITC publishes homeless counts by census tract, not point locations, so homeless locations can’t be directly linked to specific parcels. Instead, his analysis allocates homeless in a tract proportionally to the parcels in the tract. So, if a tract is 50% single-family residential, 50% of the homeless in the tract are assigned to the single-family residential portion of that tract.

It’s commonly assumed that the homeless cluster in industrial or commercial areas, such as downtowns, but the largest number of homeless is actually in residential areas. The homeless are not paricularly concentrated in residential areas, but rather, residential areas are the most common land use. Excluding military bases, state parks, peserves, single and multi-family residential areas are about 38% percent of the lands use in the Los Angeles homelessness count area, and 74% of the land use in the City of Los Angeles.

![](/uploads/4/2019/01/2c640a94-03b3-4dee-ac8b-8b17346c8227-output_15_0-1.png)

Here is the full table of the areas of the top land use codes, in percentage of all parcel area, in the City of Los Angeles, excluding regional parks, military bases, preserves and other open space ( excluded codes: 1830, 1860, 1800, 1270, 1850, 1880)

| Area (Acres)| Land Use Code  
---|---|---  
code| |   
1110| 56.777506| 1110 Single Family Residential  
1120| 17.122042| 1120 Multi-Family Residential  
1240| 5.742725| 1240 Public Facilities  
1310| 4.158022| 1310 Light Industrial  
1410| 3.487405| 1410 Transportation  
1220| 2.640562| 1220 Retail and Commercial and Services  
1311| 2.567764| 1311 Light Manufacturing  
1200| 2.366987| 1200 General Commercial  
1321| 2.208865| 1321 Heavy Manufacturing  
1221| 1.174566| 1221 Regional Shopping Center  
  
Although the largest number of homeless are counted in residential areas, they are very spread out, so the density in residential areas is relatively lower. The highest density areas are regional shopping areas, and, oddly, heavy manufacturing.

![](/uploads/4/2019/01/2c640a94-03b3-4dee-ac8b-8b17346c8227-output_19_0-1.png)

However, the association between shopping areas and industrial areas and homeless may not be a direct realtionship, but rather based on the location of Skid Row, which is near the highest concentration of parcels marked as regional shopping in the county — the Financial District, historic Downtown, Little Tokyo, Little China and Wilshire.

This map overlays the center points of parcels on the map of the top 50 highest homeless density tracts ( colored areas). The parcel points are colored by parcel type:

  * Green: 1221 Regional Shopping Center
  * Blue: 1321 Heavy Manufacturing
  * Red: 1310 Light Industrial


Note that there are many places where tracts are in the top 50 that have a high shopping density and low homeless density, or a high homelss density and low shopping density. The yellow tract is the southern portion of Skid Row. Skid Rows doesn’t have the high-density land use types in it, but

[![Homelessness-land-use-top-50.png](/uploads/4/2019/01/Homelessness-land-use-top-50.png)](</uploads/4/2019/01/Homelessness-land-use-top-50.png>)

(Click to expand the image)

Here is a similar map, but for each of the land use types, the tract that contains it is colored by the density of homeless in that tract. Note that the highest densities of homeless ( darker region color ) appears to correlate with higher parcel density ( closer dots of the same color. )

[![Homelessness-land-use.png](/uploads/4/2019/01/Homelessness-land-use-2.png)](</uploads/4/2019/01/Homelessness-land-use-2.png>)

(Click to expand the image)

# Homeless By Community[¶](</los-angeles-homelessness-by-land-use/#Homeless-By-Community>)

As can be seen in the preceeding maps, the largest number of homeless are in the Skid Row and Downtown Los Angeles areas. Surprisingly, the third largest popultion is in Antelope Valley, the area of Lancaster and Palmdale, north of the San Gabriel mountains.

| totunsheltpeople  
---|---  
community_name|   
Skid Row| 2092.0  
Downtown Los Angeles| 1462.0  
Unincorporated Antelope Valley| 1280.0  
North Hollywood| 1011.0  
Hollywood| 990.0  
Lancaster| 903.0  
South Park| 817.0  
Florence-Graham| 729.0  
Venice| 728.0  
Vermont Square| 724.0  
Santa Monica| 718.0  
Westlake| 707.0  
Pomona| 585.0  
El Monte| 514.0  
Sun Valley| 505.0  
Echo Park| 488.0  
South Central| 476.0  
Wilmington| 473.0  
Carson| 461.0  
Boyle Heights| 452.0  
Willowbrook| 403.0  
Sylmar| 399.0  
Chinatown| 387.0  
Highland Park| 384.0  
San Pedro| 378.0  
  
Dividing up the homeless counts by community and land use codes shows that the Skid Row allocation is dominated by light industrial, and that the rural residential allocation is primarily Antelope Valley. In most other places, the dominant land use is single and multi-family residential.

| code_name| community_name| totunsheltpeople  
---|---|---|---  
1319| 1310 Light Industrial| Skid Row| 1112.0  
483| 1150 Rural Residential| Unincorporated Antelope Valley| 1026.0  
1283| 1310 Light Industrial| Downtown Los Angeles| 625.0  
343| 1120 Multi-Family Residential| South Park| 500.0  
272| 1120 Multi-Family Residential| Hollywood| 476.0  
114| 1110 Single Family Residential| North Hollywood| 461.0  
93| 1110 Single Family Residential| Lancaster| 451.0  
363| 1120 Multi-Family Residential| Venice| 369.0  
364| 1120 Multi-Family Residential| Vermont Square| 364.0  
421| 1140 Mixed Residential| Florence-Graham| 358.0  
  
Dividing up the homeless of Skid Row proportionally to parcel area puts the largest portion of Skid Row homeless in light industrial and shopping areas.

| code_name| community_name| totunsheltpeople  
---|---|---|---  
1319| 1310 Light Industrial| Skid Row| 1112.0  
910| 1221 Regional Shopping Center| Skid Row| 348.0  
339| 1120 Multi-Family Residential| Skid Row| 312.0  
840| 1220 Retail and Commercial and Services| Skid Row| 188.0  
1091| 1240 Public Facilities| Skid Row| 90.0  
1863| 1800 Open Space and Recreation| Skid Row| 43.0
