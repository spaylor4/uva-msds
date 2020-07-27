#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework: Python and Web Scraper
Shannon Paylor
sep4hy
"""

#resources referenced:
#https://programminghistorian.org/en/lessons/intro-to-beautiful-soup
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://seaborn.pydata.org/index.html

from bs4 import BeautifulSoup
import requests
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#have two types of pages I want to scrape
#so creating a parent class to handle init/str methods, which are the same for both
class SoupWebpage:
    def __init__(self, url, soup = None):
        #url is string link to article
        #soup is beautiful soup html of article page
        self.url = url
        if soup is None:
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
        self.soup = soup
        
    def __str__(self):
        return self.url
        #soup is messy so don't want to include that in printing
    
#want to scrape links to articles on Motley Fool homepage
#creating as subclass of generic SoupWebpage
class MotleyFoolHomepage(SoupWebpage):
    def __init__(self, url = "https://www.fool.com", soup = None):
        SoupWebpage.__init__(self, url, soup)
        self.trend_links = [] #will be set by scrape_trending_links function
        self.trend_articles = [] #will be set by scrape_stock_mentions function
        #want homepage to have lists of links and MotleyFoolArticle objects
        #but those need to be scraped so won't have any data on instantiation
        self.article_mentions = pd.DataFrame({"title": [], "author": [], "author_username": [], "article_date": [], 
                                   "company": [], "stock_symbol": [], "quote_link": [], "article_link": []})
        #will be set by scrape_stock_mentions function
        #want to set article_mentions to the df with data scraped for all trend_links
        
    def scrape_trending_links(self):
        #returns list of links to trending articles on Motley Fool homepage
        trending = self.soup.findAll(class_ = "hp-trending-articles-list")[0]

        trending_articles = trending.findAll("a")
        
        trending_links = []
        for article in trending_articles:
            link = article.get("href")
            trending_links.append(self.url + link)
            
        self.trend_links = trending_links
        return trending_links
    
    def scrape_stock_mentions(self, already_scraped = None):
        #already_scraped is an optional df containing previously scraped data
        #this will prevent duplication of data
        
        #if no already_scraped df provided, create an empty df
        if already_scraped is None:
            already_scraped = pd.DataFrame({"title": [], "author": [], "author_username": [], "article_date": [], 
                                   "company": [], "stock_symbol": [], "quote_link": [], "article_link": []})
        
        #if no links have been scraped yet, won't be able to scrape any articles
        if len(self.trend_links) == 0:
            print('No links to scrape yet. Please run scrape_trending_links() first.')
        else:
            for link in self.trend_links:
                if link in already_scraped['article_link'].unique():
                    print('Already scraped ' + link)
                else:
                    print('Scraping ' + link)
                    article = MotleyFoolArticle(link)
                    self.trend_articles.append(article)
                    art_df = article.scrape_stocks()
                
                    self.article_mentions = self.article_mentions.append(art_df)
                    
            return self.article_mentions
        
    def get_watchlist_articles(self, watchlist):
        #watchlist should be a list of stock symbols
        #self.article_mentions needs to be already populated for this to work
        if self.article_mentions.shape[0] == 0:
            message = 'No articles have been scraped yet.'
            print(message)
            return message
        elif any(item in watchlist for item in self.article_mentions['stock_symbol']):
            watch_df = self.article_mentions[self.article_mentions['stock_symbol'].isin(watchlist)]
            watch_df = watch_df[['title', 'article_link']].drop_duplicates() #want unique articles, not all stocks mentioned
            
            message = 'Here are current Motley Fool trending articles mentioning stocks in your watchlist:\n'
            for index, row in watch_df.iterrows():
                message  = message + row['title'] + ": " + row['article_link'] + "\n"
                
            print(message)
            return message
        else:
            message = "No stocks on your watchlist were mentioned in the trending articles."
            print(message)
            return message

#after scraping links to articles, want to scrape stock mentions from within those articles
#another subclass of SoupWebpage
class MotleyFoolArticle(SoupWebpage):
    def __init__(self, url, soup = None):
        SoupWebpage.__init__(self, url, soup)
        
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
                                    "article_link": [self.url]})
            
            article_df = article_df.append(tckr_df)
            
        return article_df




### main functionality ###

#create homepage instance
homepage_url = "https://www.fool.com"
homepage = MotleyFoolHomepage(homepage_url)

#get trending links from homepage
links = homepage.scrape_trending_links()

filename = "motley_fool_stock_mentions.csv"
#if file already exists, read in existing data; if not, create an empty df to store data in
try:
    stocks_mentioned = pd.read_csv(filename)
except:
    stocks_mentioned = pd.DataFrame({"title": [], "author": [], "author_username": [], "article_date": [], 
                                   "company": [], "stock_symbol": [], "quote_link": [], "article_link": []})

#scrape stocks mentioned in articles
new_mentions = homepage.scrape_stock_mentions(stocks_mentioned)

#update and export data
stocks_mentioned = stocks_mentioned.append(new_mentions)
stocks_mentioned.to_csv(filename, index = False)

#check for articles about watchlist stocks
homepage.get_watchlist_articles(['AMZN', 'AAPL'])


### create plots for report ###
#bar chart
motley = pd.read_csv("motley_fool_stock_mentions.csv")

top10 = motley.groupby('stock_symbol')['company'].count().reset_index().sort_values(by = "company", ascending = False).head(10)
top10 = top10.rename(columns = {'company': 'mentions'})

sns.set_style("white")
ax = sns.barplot(x = "stock_symbol", y = "mentions", data = top10, color=sns.xkcd_rgb['light blue'])
sns.despine()

#heatmap
motley['date'] = pd.to_datetime(motley['article_date']).dt.strftime('%d-%m-%Y')
daily_mentions = motley.groupby(['date', 'stock_symbol'])['company'].count().reset_index()
daily_mentions = daily_mentions.rename(columns = {'company': 'mentions'})

sns.set(rc={'figure.figsize':(16.7,5.27)})

ax = sns.heatmap(daily_mentions.pivot(index = 'date', columns = 'stock_symbol', values = 'mentions'), 
            cmap = "Blues", vmin=0, vmax=daily_mentions['mentions'].max(), linewidths=0.2)

colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0, 1, 2])
colorbar.set_ticklabels(['0', '1', '2'])

ax.set_ylabel('Date')
ax.set_xlabel('Stock')

plt.show()















