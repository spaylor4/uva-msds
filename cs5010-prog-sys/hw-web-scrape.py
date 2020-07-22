#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework: Python and Web Scraper
Shannon Paylor
sep4hy
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.fool.com/investing/2020/07/21/3-growth-stocks-robinhood-investors-cant-stop-buyi.aspx"

#get html from url
r = requests.get(url)
soup = BeautifulSoup(r.text)

#extract article title
title = soup.find("h1").contents[0]

#extract article publication date
pub_dt = soup.findAll("div", "publication-date")
pub_dt = pub_dt[0].find("svg").next_sibling.strip()

#extract article author info
author = soup.findAll("div", "author-name")
author_name = author[0].findAll("a")[0].contents[0]
author_usrnm = author[0].findAll("div", class_ = "author-username")[0].contents[0]
author_usrnm = author_usrnm.strip().replace("(", "").replace(")", "")

#extract tickers
tickers = soup.findAll("span", class_ = "ticker", attrs={'data-id': False})
#tickers show up twice: in article text and in related tickers sidebar; data-id present in p but absent in table

#create empty dataframe to store article info
article_df = pd.DataFrame({"title": [], "author": [], "author_username": [], "article_date": [], 
                           "company": [], "stock_symbol": [], "quote_link": [], "article_link": []})

#extract stock info
for ticker in tickers:
    tckr = ticker.findAll("a")[0]
    quote_link = tckr.get("href")
    company = tckr.get("title")
    symbol = ticker.findAll("span", class_ = "symbol")[0].contents[0]
    
    tckr_df = pd.DataFrame({"title": [title], "author": [author_name], 
                            "author_username": [author_usrnm], 
                            "article_date": [pub_dt], 
                            "company": [company], 
                            "stock_symbol": [symbol], 
                            "quote_link": [quote_link], 
                            "article_link": [url]})
    
    article_df = article_df.append(tckr_df)



