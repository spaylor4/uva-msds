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
  



class MotleyFoolArticle:
    def __init__(self, url, soup = None):
        #url is string link to article
        #soup is beautiful soup html of article page
        self.url = url
        if soup is None:
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
        self.soup = soup
        
    def scrape_stocks(self):
        
        title = self.soup.find("h1").contents[0]
        
        #extract article publication date
        pub_dt = self.soup.findAll("div", "publication-date")
        pub_dt = pub_dt[0].find("svg").next_sibling.strip()
        
        #extract article author info
        author = self.soup.findAll("div", "author-name")
        author_name = author[0].findAll("a")[0].contents[0]
        author_usrnm = author[0].findAll("div", class_ = "author-username")[0].contents[0]
        author_usrnm = author_usrnm.strip().replace("(", "").replace(")", "")
        
        #extract tickers
        tickers = self.soup.findAll("span", class_ = "ticker", attrs={'data-id': False})
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
            
        return article_df

art1 = MotleyFoolArticle(url)
art1_df = art1.scrape_stocks()


# scrape articles off homepage

class MotleyFoolHomepage:
    def __init__(self, url, soup = None):
        #url is string link to article
        #soup is beautiful soup html of article page
        self.url = url
        if soup is None:
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
        self.soup = soup
        
    def scrape_trending_links(self):
        trending = self.soup.findAll(class_ = "hp-trending-articles-list")[0]

        trending_articles = trending.findAll("a")
        
        trending_links = []
        for article in trending_articles:
            link = article.get("href")
            trending_links.append(self.url + link)
            
        return trending_links
        

homepage_url = "https://www.fool.com"
homepage = MotleyFoolHomepage(homepage_url)

links = homepage.scrape_trending_links()



















