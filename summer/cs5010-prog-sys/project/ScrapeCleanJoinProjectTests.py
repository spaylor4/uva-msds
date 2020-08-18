#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CS 5010 Semster Project Unit Tests

Team CATS: Congxin (David) Xu, Alex Stern, Taylor Rohrich, Shannon Paylor

Computing IDs: cx2rx, acs4wq, trr2as, sep4hy
"""

import unittest
from scraper import scrapeData
import pandas as pd

#### Testing: Web Scraping
## Please note: this testcase WILL NOT run in the notebook. Please refer to the attached zip file for the scraper code and testing class.
class TestScraping(unittest.TestCase):

    # make sure invalid year returns -1 sentinel value
    def test_if_returns_sentinel_on_invalid_year(self):
        self.assertEqual(scrapeData('test', ('blah', 'foo')), -1)

    # make sure equal years returns -1 sentinel value
    def test_if_returns_sentinel_on_equal_years(self):
        self.assertEqual(scrapeData('test', (2015, 2015)), -1)

    # make sure start year greater than end year returns -1 sentinel value
    def test_if_returns_sentinel_on_start_year_greater_than_end_year(self):
        self.assertEqual(scrapeData('test', (2016, 2015)), -1)

    # make sure years outside of 1993-2019 returns -1 sentinel value

    def test_if_returns_sentinel_on_out_of_bounds_years(self):
        # greater than 2020 should fail
        self.assertEqual(scrapeData('test', (2000, 2020)), -1)
        # below 1990 should fail
        self.assertEqual(scrapeData('test', (1990, 2005)), -1)

    # make sure valid input create csv with proper amount of lines
    def test_if_csv_generated_on_valid_input(self):
        scrapeData('test', (2015, 2016))
        # Check if csv gets generated
        with open("test.csv") as f:
            # Ensure it has the correct number of lines
            self.assertEqual(len(f.readlines()), 3283)

####Testing: Exploratory Data Analysis
##note: these tests ran successfully in our notebook, but will not run here without loading the airfares csv in as "data"
class TestDataFrame(unittest.TestCase):
  
  # Make sure we are dealing with the correct dataframe with proper amount of rows
    def test_if_data_has_correct_num_rows(self):
        self.assertEqual(len(data), 35985)
  
  # Make sure our dataframe has the correct columns
    def test_if_data_has_correct_columns(self):
    
        # What the columns should be
        properColumns = ['passenger_rank', 'airport_code', 'city_name', 
                         'state_name', 'avg_fare', 'avg_fare_adjusted', 
                         'year', 'quarter', 'state_city', 'year_quarter',
                         'quarter_month', 'date']
        # make sure that the columns match  
        for i, col in enumerate(data.columns):
            self.assertEqual(col, properColumns[i])

  # Make sure that we do not have any missing values in the data
    def test_that_there_are_no_nas(self):

        # IsNa will return booleans for if the element is na or not. Since False is implicitly 0, we want the sum of all the rows, columns to be 0
        self.assertEqual(data.isna().sum().sum(),0)

  # Ensure we have data only from 2000 - 2019
    def test_that_data_is_in_correct_time_range(self):

        # Get unique years
        uniqueYears = set(data['year'])

        # Ensure that each year is in the appropriate interval
        for year in uniqueYears:
            self.assertTrue(1999 < year < 2020)

  # Ensure the data has the proper number of airport codes
    def test_that_data_has_proper_num_aircodes(self):

        # Get unique airport codes, should be equal to 690
        self.assertEqual(len(set(data['airport_code'])), 690)

  # Test to see if the concatenation works correctly for all dates
    def test_that_data_has_year_quarter_combination_for_correct_time_range(self):

        # Get the year quarter combinations from data
        yearQuarterCombos = set(data['year_quarter'])

        for year in range(2000,2020):
            for quarter in range(1,5):
                # Validate that all of these combinations are in the data
                self.assertTrue(f'{year}_{quarter}' in yearQuarterCombos)
  
  # Test to see if the fill table contains the correct number of rows 
  # fill table is later append to the main table and it should only contains
  # the missing data for each airport with 79 records
    def test_fill_table_contains_correct_records(self):
        tmp = data[['airport_code', 'year', 'quarter']].groupby('airport_code').agg('count')
        tmp.reset_index(inplace=True)
        tmp = tmp[tmp['quarter'] == 79]

        # Since we only have 1 period missing, the number of records in the fill 
        # table should equal to the number of records with 79 periods of records
        self.assertEqual(len(fill), len(tmp))

  # Test to see if data_clean have the right records
    def test_data_clean_records(self):
        tmp = data_clean[['airport_code', 'year', 'quarter']].groupby('airport_code').agg('count')
        tmp.reset_index(inplace=True)

        # After cleaning, each airport_code should have 80 records
        # That means no airports should have a different number of records
        self.assertEqual(len(tmp[tmp['quarter'] != 80]), 0)

    def test_fare_dtypes(self):
        #test that fare colmns were correctly converted to numeric
        self.assertTrue(pd.api.types.is_numeric_dtype(data['avg_fare']))
        self.assertTrue(pd.api.types.is_numeric_dtype(data['avg_fare_adjusted']))


#### Testing: Joining Data
class TestAirfareDataJoins(unittest.TestCase):
    def test_airfare_pivot(self):
        #make sure pivoting to get separate columns for 2010 and 2019 fares gives expected number of rows
#         msa_lkp = pd.read_csv("/content/drive/My Drive/msa_lookup.csv", encoding = 'latin1')
#         popul = pd.read_csv("/content/drive/My Drive/cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp = pd.read_csv("msa_lookup.csv", encoding = 'latin1')
        popul = pd.read_csv("cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp.drop("Unnamed: 10", axis = 1, inplace = True)
        msa_lkp.columns = msa_lkp.columns.str.lower()
        #want only airports; dataset contains bus stops and others
        msa_lkp = msa_lkp[msa_lkp['airport_code'].notnull()]
        popul = popul[['CBSA', 'NAME', 'LSAD', 'CENSUS2010POP', 'POPESTIMATE2019']]
        popul = popul.rename(columns = {'CBSA': 'cbsa_code', 'CENSUS2010POP': 'pop_2010', 'POPESTIMATE2019': 'pop_2019'})
        popul.columns = popul.columns.str.lower()
        #cbsa not unique (has MSA and counties within MSA)
        popul = popul[popul['lsad'].isin(['Metropolitan Statistical Area', 'Micropolitan Statistical Area'])]


#         data = pd.read_csv("/content/drive/My Drive/airfares_final.csv")
        data = pd.read_csv("airfares_final.csv")
        data = data.rename(columns = {'average_fair': 'avg_fare', 'average_fair_adjusted': 'avg_fare_adjusted'})
        #convert fares to numeric
        data[['avg_fare', 'avg_fare_adjusted']] = data[['avg_fare', 'avg_fare_adjusted']].apply(lambda x: x.str.replace(',', '').astype(float))
        
        #get number of airports with data for either 2010 or 2019 Q1
        num_airports = data[(data['year'].isin([2010, 2019])) & (data['quarter'] == 1)]['airport_code'].nunique()
        
        #perform pivot
        air_pop = data[(data['year'].isin([2010, 2019])) & (data['quarter'] == 1)].pivot_table(index = ['airport_code', 'city_name', 'state_name'], 
                                                                                                   columns = 'year', values = ['avg_fare', 'avg_fare_adjusted'])
       
        #check that pivot number of rows = number of airports
        self.assertEqual(num_airports, air_pop.shape[0])
    
    def test_join_msa(self):
        #make sure joining with msa table doesn't duplicate rows
        #perform step tested by previous unit test
#         msa_lkp = pd.read_csv("/content/drive/My Drive/msa_lookup.csv", encoding = 'latin1')
#         popul = pd.read_csv("/content/drive/My Drive/cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp = pd.read_csv("msa_lookup.csv", encoding = 'latin1')
        popul = pd.read_csv("cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp.drop("Unnamed: 10", axis = 1, inplace = True)
        msa_lkp.columns = msa_lkp.columns.str.lower()
        #want only airports; dataset contains bus stops and others
        msa_lkp = msa_lkp[msa_lkp['airport_code'].notnull()]
        popul = popul[['CBSA', 'NAME', 'LSAD', 'CENSUS2010POP', 'POPESTIMATE2019']]
        popul = popul.rename(columns = {'CBSA': 'cbsa_code', 'CENSUS2010POP': 'pop_2010', 'POPESTIMATE2019': 'pop_2019'})
        popul.columns = popul.columns.str.lower()
        #cbsa not unique (has MSA and counties within MSA)
        popul = popul[popul['lsad'].isin(['Metropolitan Statistical Area', 'Micropolitan Statistical Area'])]

#         data = pd.read_csv("/content/drive/My Drive/airfares_final.csv")
        data = pd.read_csv("airfares_final.csv")
        data = data.rename(columns = {'average_fair': 'avg_fare', 'average_fair_adjusted': 'avg_fare_adjusted'})
        #convert fares to numeric
        data[['avg_fare', 'avg_fare_adjusted']] = data[['avg_fare', 'avg_fare_adjusted']].apply(lambda x: x.str.replace(',', '').astype(float))
        air_pop = data[(data['year'].isin([2010, 2019])) & (data['quarter'] == 1)].pivot_table(index = ['airport_code', 'city_name', 'state_name'], 
                                                                                                   columns = 'year', values = ['avg_fare', 'avg_fare_adjusted'])
        air_pop.columns = ['{}_{}'.format(i, j) for i, j in air_pop.columns]
        air_pop = air_pop.reset_index()
        
        #save original number of rows for later comparison
        start_rows = air_pop.shape[0]
        
        #perform the join
        air_pop = pd.merge(air_pop, msa_lkp, how = 'left', on = 'airport_code')
        
        #check that we have the same number of rows that we started with
        self.assertEqual(start_rows, air_pop.shape[0])
        
    def test_join_population(self):
        #make sure joining with population table doesn't duplicate rows
        #perform previously tested pivot/join
#         msa_lkp = pd.read_csv("/content/drive/My Drive/msa_lookup.csv", encoding = 'latin1')
#         popul = pd.read_csv("/content/drive/My Drive/cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp = pd.read_csv("msa_lookup.csv", encoding = 'latin1')
        popul = pd.read_csv("cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp.drop("Unnamed: 10", axis = 1, inplace = True)
        msa_lkp.columns = msa_lkp.columns.str.lower()
        #want only airports; dataset contains bus stops and others
        msa_lkp = msa_lkp[msa_lkp['airport_code'].notnull()]
        popul = popul[['CBSA', 'NAME', 'LSAD', 'CENSUS2010POP', 'POPESTIMATE2019']]
        popul = popul.rename(columns = {'CBSA': 'cbsa_code', 'CENSUS2010POP': 'pop_2010', 'POPESTIMATE2019': 'pop_2019'})
        popul.columns = popul.columns.str.lower()
        #cbsa not unique (has MSA and counties within MSA)
        popul = popul[popul['lsad'].isin(['Metropolitan Statistical Area', 'Micropolitan Statistical Area'])]

#         data = pd.read_csv("/content/drive/My Drive/airfares_final.csv")
        data = pd.read_csv("airfares_final.csv")
        data = data.rename(columns = {'average_fair': 'avg_fare', 'average_fair_adjusted': 'avg_fare_adjusted'})
        #convert fares to numeric
        data[['avg_fare', 'avg_fare_adjusted']] = data[['avg_fare', 'avg_fare_adjusted']].apply(lambda x: x.str.replace(',', '').astype(float))
        air_pop = data[(data['year'].isin([2010, 2019])) & (data['quarter'] == 1)].pivot_table(index = ['airport_code', 'city_name', 'state_name'], 
                                                                                                   columns = 'year', values = ['avg_fare', 'avg_fare_adjusted'])
        air_pop.columns = ['{}_{}'.format(i, j) for i, j in air_pop.columns]
        air_pop = air_pop.reset_index()
        
        air_pop = pd.merge(air_pop, msa_lkp, how = 'left', on = 'airport_code')
        
        #save original number of rows for later comparison
        start_rows = air_pop.shape[0]

        #perform the join
        air_pop = pd.merge(air_pop, popul, how = 'left', on = 'cbsa_code') #some MSAs are in the pop data multiple times
        
        #check that we have the same number of rows that we started with
        self.assertEqual(start_rows, air_pop.shape[0])
        
    def test_dropna(self):
        #make sure final df has no nulls for any of the four fare columns
#         msa_lkp = pd.read_csv("/content/drive/My Drive/msa_lookup.csv", encoding = 'latin1')
#         popul = pd.read_csv("/content/drive/My Drive/cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp = pd.read_csv("msa_lookup.csv", encoding = 'latin1')
        popul = pd.read_csv("cbsa_pop_est2019.csv", encoding = 'latin1')
        msa_lkp.drop("Unnamed: 10", axis = 1, inplace = True)
        msa_lkp.columns = msa_lkp.columns.str.lower()
        #want only airports; dataset contains bus stops and others
        msa_lkp = msa_lkp[msa_lkp['airport_code'].notnull()]
        popul = popul[['CBSA', 'NAME', 'LSAD', 'CENSUS2010POP', 'POPESTIMATE2019']]
        popul = popul.rename(columns = {'CBSA': 'cbsa_code', 'CENSUS2010POP': 'pop_2010', 'POPESTIMATE2019': 'pop_2019'})
        popul.columns = popul.columns.str.lower()
        #cbsa not unique (has MSA and counties within MSA)
        popul = popul[popul['lsad'].isin(['Metropolitan Statistical Area', 'Micropolitan Statistical Area'])]

#         data = pd.read_csv("/content/drive/My Drive/airfares_final.csv")
        data = pd.read_csv("airfares_final.csv")
        data = data.rename(columns = {'average_fair': 'avg_fare', 'average_fair_adjusted': 'avg_fare_adjusted'})
        #convert fares to numeric
        data[['avg_fare', 'avg_fare_adjusted']] = data[['avg_fare', 'avg_fare_adjusted']].apply(lambda x: x.str.replace(',', '').astype(float))
        air_pop = data[(data['year'].isin([2010, 2019])) & (data['quarter'] == 1)].pivot_table(index = ['airport_code', 'city_name', 'state_name'], 
                                                                                                   columns = 'year', values = ['avg_fare', 'avg_fare_adjusted'])
        air_pop.columns = ['{}_{}'.format(i, j) for i, j in air_pop.columns]
        air_pop = air_pop.reset_index()
        
        air_pop = pd.merge(air_pop, msa_lkp, how = 'left', on = 'airport_code')
        
        air_pop = pd.merge(air_pop, popul, how = 'left', on = 'cbsa_code') #some MSAs are in the pop data multiple times
        
        air_pop = air_pop.dropna()
        
        fares_na = air_pop[(air_pop['avg_fare_2010'].isna()) | (air_pop['avg_fare_2019'].isna()) | (air_pop['avg_fare_adjusted_2010'].isna()) | (air_pop['avg_fare_adjusted_2019'].isna())]
        
        self.assertEqual(fares_na.shape[0], 0)



if __name__ == "__main__":
    unittest.main()


