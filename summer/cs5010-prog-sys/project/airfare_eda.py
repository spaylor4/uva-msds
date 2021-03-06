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

import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
import seaborn as sns

### Read in Data -----------------------------------------------

airfares = pd.read_csv("airfares_final.csv")

msa_lkp = pd.read_csv("msa_lookup.csv", encoding = 'latin1')

popul = pd.read_csv("cbsa_pop_est2019.csv", encoding = 'latin1')


### Cleaning ---------------------------------------------------

## airfares data
airfares = airfares.rename(columns = {'average_fair': 'avg_fare', 'average_fair_adjusted': 'avg_fare_adjusted'}) #personal preference

#convert fares to numeric
airfares[['avg_fare', 'avg_fare_adjusted']] = airfares[['avg_fare', 'avg_fare_adjusted']].apply(lambda x: x.str.replace(',', '').astype(float))

#add date column (first day of quarter) for use in plot
airfares['quarter_month'] = np.select([airfares['quarter'] == 1, airfares['quarter'] == 2, airfares['quarter'] == 3, airfares['quarter'] == 4], choicelist = [1, 4, 7, 10])
airfares['date'] = airfares.apply(lambda row: dt.date(row['year'], row['quarter_month'], 1), axis=1)

def date_from_quarter(df, quarter_col = "quarter", year_col = "year"):
    #take a df with quarter & year columns (names of columns are inputs)
    #return a date column with date equal to first day of quarter
    df['quarter_month'] = np.select([df[quarter_col] == 1, df[quarter_col] == 2, df[quarter_col] == 3, df[quarter_col] == 4], choicelist = [1, 4, 7, 10])
    date_col = df.apply(lambda row: dt.date(row[year_col], row['quarter_month'], 1), axis=1)

    return date_col
    

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

#cbsa not unique (has MSA and counties within MSA)
popul = popul[popul['lsad'].isin(['Metropolitan Statistical Area', 'Micropolitan Statistical Area'])]

#now is cbsa unique?
popul.groupby('cbsa_code')['name'].nunique().reset_index().sort_values(by = 'name', ascending = False)
#yep

### Joining --------------------------------------------------

sum(msa_lkp['cbsa_code'].isin(popul['CBSA'])) #how many MSAs have population data?
sum(airfares['airport_code'].isin(msa_lkp['airport_code']))
airfares['airport_code'].nunique()

#for population exploration, only want Q1 2010 & 2019 data

air_pop = airfares[(airfares['year'].isin([2010, 2019])) & (airfares['quarter'] == 1)].pivot_table(index = ['airport_code', 'city_name', 'state_name'], 
                                                                                                   columns = 'year', values = ['avg_fare', 'avg_fare_adjusted'])
air_pop.columns = ['{}_{}'.format(i, j) for i, j in air_pop.columns]
air_pop = air_pop.reset_index()

air_pop = pd.merge(air_pop, msa_lkp, how = 'left', on = 'airport_code')

air_pop = pd.merge(air_pop, popul, how = 'left', on = 'cbsa_code') #some MSAs are in the pop data multiple times

air_pop = air_pop.dropna()

### Compare Population & Price -------------------------------

# #simple scatter plot
# fig = px.scatter(data_frame = air_pop, x = "pop_2019", y = "avg_fare_2019")
# plot(fig)

#scatter with log axes
fig = go.Figure()
fig.add_trace(go.Scatter(x = air_pop["pop_2019"], y = air_pop["avg_fare_2019"], mode = 'markers'))
fig.update_layout(title = "Average Airfare vs. Population, 2019", 
                  xaxis_title = "Population, Local MSA", yaxis_title = "Average Q1 Airfare")

# fig.update_layout(xaxis_type="log", yaxis_type="log")

plot(fig)

#calculate simple correlation
air_pop["pop_2019"].corr(air_pop['avg_fare_2019'])

#what about passenger rank vs. fare?
ranked = airfares[(airfares['year']==2019) & (airfares['quarter'] == 1)]

ranked['passenger_rank'].corr(ranked['avg_fare'])

fig = go.Figure()
fig.add_trace(go.Scatter(x = ranked["passenger_rank"], y = ranked["avg_fare"], mode = 'markers'))
fig.update_layout(title = "Average Airfare vs. Passenger Rank, 2019", 
                  xaxis_title = "Passenger Rank", yaxis_title = "Average Q1 Airfare")
fig.update_xaxes(range = [max(ranked['passenger_rank']), 1])

plot(fig)


### Animate Transition from Regular to Log Axis --------------

fig = go.Figure(data = [go.Scatter(x = air_pop["pop_2019"], y = air_pop["avg_fare_2019"], mode = 'markers')], 
                layout = go.Layout(title="Start Title", 
                                   updatemenus=[dict(
                                        type="buttons",
                                        buttons=[dict(label="Play",
                                                      method="animate",
                                                      args=[None])])] ), 
                frames = [go.Frame(data = [go.Scatter(x = air_pop["pop_2019"], y = air_pop["avg_fare_2019"], mode = 'markers')], 
                                   layout=go.Layout(xaxis_type="linear", yaxis_type="linear")), 
                          go.Frame(data = [go.Scatter(x = air_pop["pop_2019"], y = air_pop["avg_fare_2019"], mode = 'markers')], 
                                   layout=go.Layout(xaxis = dict(type = 'log', range = [np.log10(10000), np.log10(20000000)]), 
                                                    yaxis = dict(type = 'log', range = [2, np.log10(1000)]))
                    )]
                )

# fig.update_layout(title = "Average Airfare vs. Passenger Rank, 2019", 
#                   xaxis_title = "Passenger Rank", yaxis_title = "Average Q1 Airfare")
# fig.update_xaxes(range = [max(ranked['passenger_rank']), 1])
fig.update_layout(transition_duration=3000)

plot(fig)


####



### Time Series Plot -----------------------------------------

#basic plot with all airports (messy)
# fig = px.line(airfares, x = 'date', y = 'avg_fare', color = 'airport_code',
#               color_discrete_sequence = pd.Series(np.repeat('darkgray', airfares.shape[0])))

# plot(fig)


#go plot with selected airports
#https://towardsdatascience.com/getting-started-with-plot-ly-3c73706a837c

airports = ["LAX", "ORD", "DEN", "IAD", "BOS"]
colors = dict(zip(airports, sns.color_palette("GnBu_d", len(airports)).as_hex()))

trace_list = []
for airport in airports:
    trace = go.Scatter(
        y = airfares[airfares['airport_code']==airport]['avg_fare_adjusted'].tolist(),
        x = airfares[airfares['airport_code']==airport]['date'].tolist(),
        mode = 'lines',
        name = airport,
        line = dict(
                    color = colors[airport],
                    width = 1.5
#                    dash = 'dot'
                    ), 
        hovertemplate = '<br>%{x}<br>' + 'Price: $%{y:.2f}'
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

### Prediction Plots -------------------------------------------
from plotly.subplots import make_subplots

time_series_plot_df = pd.read_csv()

time_series_plot_df[['Year', 'Qtr']] = time_series_plot_df['Quarter'].str.split("_", expand = True)
time_series_plot_df['Date'] = date_from_quarter(time_series_plot_df, quarter_col="Qtr", year_col="Year")

fig = make_subplots(rows = 5, cols = 1)

fig.append_trace(go.Scatter(
    x=time_series_plot_df[(time_series_plot_df['Airport']=='LAX') & (time_series_plot_df['RealOrPrediction']=='Actual')]['Date'].tolist(),
    y=time_series_plot_df[(time_series_plot_df['Airport']=='LAX') & time_series_plot_df['RealOrPrediction']=='Actual']['Price'].tolist(),
    mode='lines',
    line = dict(
                    width = 1.5
                    )
), row=1, col=1)

fig.update_yaxes(title_text="Fare", range=[0, 475])
fig.update_xaxes(title_text="Quarter", range=[dt.date(2019, 1, 1), dt.date(2019, 12, 1)])

fig.update_layout(title_text="Actual vs. Predicted Fares, 2019", height=700)

# row_num = 1
# for airport in airport_code_list:
#   fig.append_trace(go.Scatter(
#       x=[3, 4, 5],
#       y=[1000, 1100, 1200],
#   ), row=1, col=1)

#   row_num += 1

fig.show()

