import urllib
import requests
import json
import time
import settings
import pprint
import argparse
import pandas as pd
from textblob import TextBlob
import dateparser

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

from pandas.plotting import register_matplotlib_converters
import datetime

register_matplotlib_converters()


parser = argparse.ArgumentParser(description='Scrape some Guardian articles')
parser.add_argument('query', type=str, help='Query for Guardian articles')
parser.add_argument('from_date', type=str, help='"From" date for articles in format YYYY-MM-DD')
parser.add_argument('pages', type=int, help='Number of search result pages to return.')

def sentiment_analysis(text):
    analysis = TextBlob(text)
    return analysis.polarity, analysis.subjectivity

def scrape_articles(args):

    article_db = pd.DataFrame(columns=['article_title', 'article_section', 'article_date', 'article_url', 'title_sentiment', 'title_subjectivity'])
    for page in range(1, args.pages+1):
        url = 'https://content.guardianapis.com/search?&q={}&api-key={}&from-date={}&page-size=10&page={}&order-by=relevance'.format(args.query, settings.API_KEY, args.from_date, page)
        print('scraping page ', page)
        articles = []
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
            results = data['response']['results']
            for article in results:
                date = article['apiUrl'].split('/')
                article_info = {
                'article_title' : article['webTitle'],
                'article_section' : article['sectionName'],
                'article_date' : dateparser.parse('{} {} {}'.format(date[4], date[5], date[6])),
                'article_url' : article['webUrl'],
                'title_sentiment' : sentiment_analysis(article['webTitle'])[0],
                'title_subjectivity' : sentiment_analysis(article['webTitle'])[1]
                }
                articles.append(article_info)
                print(article['webTitle'])
                article_db.loc[len(article_db)] = article_info
    return article_db


if __name__ == '__main__':
    args = parser.parse_args()
    db = scrape_articles(args)
    print(db)
    print(str(db['title_sentiment'].mean()) + ' average sentiment.')
    db.to_csv('Guardian_{}_sentiment_{}.csv'.format(args.query, datetime.datetime.now()))
