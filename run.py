import urllib
import requests
import json
import time
import settings
import pprint
import argparse
import pandas as pd
import sys

parser = argparse.ArgumentParser(description='Scrape some Guardian articles')
parser.add_argument('query', type=str, help='Query for Guardian articles')
parser.add_argument('from_date', type=str, help='"From" date for articles in format YYYY-MM-DD')
parser.add_argument('pages', type=int, help='Number of search result pages to return.')

def scrape_articles():
    args = parser.parse_args()
    article_db = pd.DataFrame(columns=['article_title', 'article_section', 'article_date', 'article_url'])
    for page in range(1, args.pages):
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
                'article_date' : '{} {} {}'.format(date[4], date[5], date[6]),
                'article_url' : article['webUrl']
                }
                articles.append(article_info)
                print(article['webTitle'])
                article_db.loc[len(article_db)] = article_info
    return article_db

if __name__ == '__main__':
    db = scrape_articles()
    print(db)
