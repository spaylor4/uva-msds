#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework: Python and Web Scraper
Shannon Paylor
sep4hy
"""

from bs4 import BeautifulSoup
import requests

url = "https://www.fool.com/investing/2020/07/21/3-growth-stocks-robinhood-investors-cant-stop-buyi.aspx"

r = requests.get(url)

soup = BeautifulSoup(r.text)

tickers = soup.findAll("span", class_ = "ticker", attrs={'data-id': False})
#tickers show up twice: in article text and in related tickers sidebar; data-id present in p but absent in table

for ticker in tickers:
    tckr = ticker.findAll("a")[0]
    quote_link = tckr.get("href")
    company = tckr.get("title")
    symbol = ticker.findAll("span", class_ = "symbol")[0].contents[0]

title = soup.find("h1").contents[0]

pub_dt = soup.findAll("div", "publication-date")
pub_dt = pub_dt[0].find("svg").next_sibling.strip()

author = soup.findAll("div", "author-name")
author_name = author[0].findAll("a")[0].contents[0]
author_usrnm = author[0].findAll("div", class_ = "author-username")[0].contents[0]
author_usrnm = author_usrnm.strip().replace("(", "").replace(")", "")

