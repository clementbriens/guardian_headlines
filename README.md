# guardian_headlines
Python Sentiment analysis of Guardian headlines

# Installation

## Clone the repo
`git clone https://github.com/clementbriens/guardian_headlines.git`
`cd guardian_headlines`
`virtualenv env -p python3`
`source env/bin/activate`
`pip install -r requirements.txt`

## Get your API Key

Sign up on https://open-platform.theguardian.com/documentation/
Add your API Key to API_KEY in settings.py


# Usage

`python run.py [query] [from date] [pages]`

Each page contains 10 results.
The script returns an average sentiment as well as a .csv file in its directory that you can use for further data visualisation.

# Example

python run.py brexit 2018-01-01 100

Returns 1000 articles with a headline containing 'brexit' starting January 1st 2018

![Example](https://github.com/clementbriens/guardian_headlines/blob/master/sentiment%20brexit.png)
