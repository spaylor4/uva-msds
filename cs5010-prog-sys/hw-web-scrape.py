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



title = soup.findAll("h1")

pub_dt = soup.findAll("div", "publication-date")

author = soup.findAll("div", "author-name")

