# Monster Job Web Scraper
[![Run on Repl.it](https://repl.it/badge/github/crc8109/job-scraper)](https://repl.it/github/crc8109/job-scraper)

A web-scrapping tool to help cut down on the noise in the job hunting process.

Pass along arguments to the script (e.g language, location, etc) to get more tailored result. It's a CLI app but I'm hosting it on Replit to make it accessible to anyone.

## What This Includes

 `job_scraper.py`: The command line app to help you scrape relevant jobs from Monster by City and Language


# Getting Started

## Requirements
* Python3
* beautifulsoup4
* requests

## Quick Start
You can go to [repl.it](https://repl.it/@crc8109/job-scraper#README.md) where I'm hosting the app in a personal repl. When you click the link, just hit the button up top that says `Run` with the forward arrow and the app will start up.

## Start from Scratch
Clone this repo. Then set your environment set up by running the following command in your terminal:
```
pip install -r requirements.txt
```
Run ```job_scraper.py``` to start scraping for jobs.

If this doesn't work, try changing your search criteria. Or, it could be Monster updated their layout of their site, so my script will need updating (the woes of web scrapping). But feel free to reach out if you need anything.
