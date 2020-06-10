# Monster Job Web Scraper

I followed a tutorial from [Real Python](https://realpython.com/beautiful-soup-web-scraper-python/) and [Martin Breuss] (https://github.com/martin-martin).

In the tutorial, they teach you about Beautiful Soup by creating a web scraper that searches Monster.com for software developer positions.

I've built upon it by allowing users to pass along arguments to the script so that users can get more tailored results, making it a command line app. You can pass along city or state and language to get the results you need. Further, you can pass along another argument (called Role) so that you can look for more relevant positions (e.g front end, data scientist, etc).

## What This Includes
There are two available scripts:

1. `tutorial-beautiful-soup-web-scraper-python.py`: The sample script from the tutorial with my additional comments to help first timers follow along easier

2. `job_web_scraper.py`: The command line app to help you scrape relevant jobs from Monster

# Getting Started

## Requirements
* Python3
* beautifulsoup4
* requests

## Quick Start
Get your environment set up by running the following commands in your terminal:
```
pip3 install beautifulsoup4
pip3 install requests
```
Then clone this repo and run ```job_web_scraper.py``` to start scraping for jobs.
