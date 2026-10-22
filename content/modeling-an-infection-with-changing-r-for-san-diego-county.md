---
title: "Modeling an Infection with Changing R for San Diego County"
date: 2022-02-01T22:04:17+00:00
draft: false
type: "post"
categories: ["COVID-19", "Health"]
tags: ["COVID-19"]
author: "publisher"
description: "The SIR infection model is a simple way of exploring the effects of a social distance policy on a large population such as San Diego County"
---

**Eric Busboom**.

_The SIR infection model is a simple way of exploring the effects of a social distance policy on a large population such as San Diego County_

[ `` Full notebook on github  
](<https://github.com/sandiegodata/covid19/blob/master/Notebooks/SIR%20Model.ipynb>)

The SIR infection model is a simple set of differential equations that describe how a disease can spread under very homogeneous, stable conditions. The model gets it's name from the three "compartments" for people in diferent conditions:

  * Susceptible: people who can be infected.
  * Infected: people who are infected.
  * Recovered or Removed: people who were infected, and can't get infected again. 


There are [many good overviews](<https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model>) of the model online, so in this brief analysis, we will just use the model to visuaize what happens when the $R$ parameter for an epidemic changes.

$R$ is the ["effective reproduction number"](<https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1a-epidemiology/epidemic-theory>) of a disease, which describes the rate of increase of infection for curent conditions. It differs from the similar number, one most people are more familliar with from recent press, the basic reproduction number $R_0$, in that $R$ can change, but $R_0$ cannot.

The SIR model doesn't use $R$ or $R_0$ directly; it uses an infection rate $\beta$ and recovery rate $\gamma$, and $R_0$ = $\frac{\beta N}{\gamma}$, where $N$ is the total population. In this simulation, we'll use the SIR model to see what happens when a population the size of San Diego County gets one infection, with one case with constant $R_0$ and other cases where $R$ changes from $R_0$ to a lower value. We will change $R$ by changing $\beta$ and leaving $\gamma$ constant, which is a simple simulation of San Diego implementing a social distancing policy.

![](/uploads/3/2022/02/88381a4c-4224-4a5e-baac-c4483a6b638e-output_7_1.png) ![](/uploads/3/2022/02/88381a4c-4224-4a5e-baac-c4483a6b638e-output_9_0.png)
