# Monster Job Web Scraper

I followed a tutorial from [Real Python](https://realpython.com/beautiful-soup-web-scraper-python/) and [Martin Breuss](https://github.com/martin-martin).

In the tutorial, they teach you about Beautiful Soup by creating a web scraper that searches Monster.com for software developer positions.

I've built upon it by allowing users to pass along arguments to the script so that users can get more tailored results, making it a command line app. You can pass along city or state and language to get the results you need. In the future, you can pass along another argument (called Role) so that you can look for more relevant positions (e.g front end, data scientist, etc).

## What This Includes
There are two available scripts:

1. `RP_Tutorial.py`: The sample script from the tutorial with my additional comments and UI changed to help first timers follow along easier

2. `job_scraper.py`: The command line app to help you scrape relevant jobs from Monster by City and Language


# Getting Started

## Requirements
* Python3
* beautifulsoup4
* requests

## Quick Start
Clone this repo. Then set your environment set up by running the following commands in your terminal:
```
pip install -r requirements.txt
```
Run ```job_scraper.py``` to start scraping for jobs.
