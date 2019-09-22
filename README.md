# guardian_headlines
Simple Python scraper for Guardian API

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

`python run.py [query] [from date] [results]`

# Example

python run.py arsenal 2018-01-01 50

Returns 50 articles with a headline containing 'arsenal' starting January 1st 2018

