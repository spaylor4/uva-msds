#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:29:45 2020

@author: shannon
"""

#population by MSA for 2010-2019 downloaded from 
#https://www.census.gov/data/tables/time-series/demo/popest/2010s-total-metro-and-micro-statistical-areas.html
#original filename cbsa-est2019-alldata, renamed to cbsa_pop_est2019

#MSA to airport lookup downloaded from 
#https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=
#original filename 144545528_T_TRANSNET_FACILITY, renamed to msa_lookup
#relevant fields are CBSA code = MSA code, airport code, long/lat
#CBSA type is 1 = METRO, 2 = MICRO, 0 = not in a CBSA

#airfares_final scraped by Taylor from BTS site

import pandas as pd
import numpy as np
import datetime as dt

### Read in Data -----------------------------------------------

airfares = pd.read_csv("airfares_final.csv")

msa_lkp = pd.read_csv("msa_lookup.csv", encoding = 'latin1')

popul = pd.read_csv("cbsa_pop_est2019.csv", encoding = 'latin1')


### Cleaning ---------------------------------------------------

## airfares data
airfares = airfares.rename(columns = {'average_fair': 'avg_fare', 'average_fair_adjusted': 'avg_fare_adj'}) #personal preference

#convert fares to numeric
airfares[['avg_fare', 'avg_fare_adj']] = airfares[['avg_fare', 'avg_fare_adj']].apply(lambda x: x.str.replace(',', '').astype(float))

#add date column (first day of quarter) for use in plot
airfares['quarter_month'] = np.select([airfares['quarter'] == 1, airfares['quarter'] == 2, airfares['quarter'] == 3, airfares['quarter'] == 4], choicelist = [1, 4, 7, 10])
airfares['date'] = airfares.apply(lambda row: dt.date(row['year'], row['quarter_month'], 1), axis=1)

##msa_lkp data
msa_lkp.drop("Unnamed: 10", axis = 1, inplace = True)

msa_lkp.columns = msa_lkp.columns.str.lower() #personal preference

#want only airports; dataset contains bus stops and others
msa_lkp = msa_lkp[msa_lkp['airport_code'].notnull()]

msa_lkp.to_csv('msa_airport_lookup.csv', index = False)

##population data

popul.info()

#for now, only care about population in 2010 and 2019 so dropping other columns
popul = popul[['CBSA', 'NAME', 'LSAD', 'CENSUS2010POP', 'POPESTIMATE2019']]

popul = popul.rename(columns = {'CBSA': 'cbsa_code', 'CENSUS2010POP': 'pop_2010', 'POPESTIMATE2019': 'pop_2019'})
popul.columns = popul.columns.str.lower()

### Joining --------------------------------------------------

sum(msa_lkp['cbsa_code'].isin(popul['CBSA'])) #how many MSAs have population data?
sum(airfares['airport_code'].isin(msa_lkp['airport_code']))
airfares['airport_code'].nunique()


pd.merge(msa_lkp, popul, how = 'left', on = 'cbsa_code').info() #some MSAs are in the pop data multiple times


### Time Series Plot -----------------------------------------

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import seaborn as sns

#basic plot with all airports (messy)
fig = px.line(airfares, x = 'date', y = 'avg_fare', color = 'airport_code',
              color_discrete_sequence = pd.Series(np.repeat('darkgray', airfares.shape[0])))

plot(fig)


#go plot with selected airports
#https://towardsdatascience.com/getting-started-with-plot-ly-3c73706a837c

airports = ["LAX", "ORD", "DEN", "ALT", "BOS"]
colors = dict(zip(airports, sns.color_palette("GnBu_d", len(airports)).as_hex()))

trace_list = []
for airport in airports:
    trace = go.Scatter(
        y = airfares[airfares['airport_code']==airport]['avg_fare_adj'].tolist(),
        x = airfares[airfares['airport_code']==airport]['date'].tolist(),
        mode = 'lines',
        name = airport,
        line = dict(
                    color = colors[airport],
                    width = 1.5
#                    dash = 'dot'
                    )
        )
    trace_list.append(trace)


layout = go.Layout(
    xaxis=dict(title='Year from 2000 to 2019', zeroline=False, rangeslider=dict(visible=True)),
    yaxis=dict(title='Average Airfare, Inflation-Adjusted', zeroline=False),

    title='Airfares for Top 5 US Airports',
    showlegend=True,
    )



fig = go.Figure(data=trace_list, layout=layout)

plot(fig)


#add figure widget functionality



