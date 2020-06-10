import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=python&where=chicago'

#pinging page for content with a 200 request
page = requests.get(URL)

#make a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#filters for targeted content only
results = soup.find(id='ResultsContainer')

def print_all_jobs(results):
    # find_all returns an iterable with all HTML for all job listings displayed on page.
    # Notice: you mention element, then class in order to use find_all
    job_elems = results.find_all('section', class_='card-content')
    print(f"Available Jobs: {len(job_elems)}")
    print("Printing all jobs:\n")

    #this will print every job posting as text
    for job_elem in job_elems:
        # each job_elem is a new BeautifulSoup object
        # you can use the same methods on it as you did before
        #link = job_elem.find('a')['href']
        title_elem = job_elem.find('h2', class_='title')
        company_elem = job_elem.find('div', class_='company')
        location_elem = job_elem.find('div', class_='location')

        #monster has a Section html element that DOESN"T have info, so without this,
        #it'll return an error with the print statements afterwards
        if None in (title_elem, company_elem, location_elem):
            continue

        # elem.text returns only text from that element, not all the HTML tag info
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(f"{location_elem.text.strip()}")
        print(f"Apply here: {job_elem.find('a')['href']}\n")
        print("-" * 75,'\n' )

def python_jobs(results):
    #string= searches for an EXACT match, so we use lower() to change all H2 text
    #to lowercase, so we can better search, removing the possiblity of some titles
    #being in upper case; it also only returns text/discards things like <a> links
    py_jobs = results.find_all('h2',
                                   string=lambda text: 'python' in text.lower())

    print(f"Available Python Jobs: {len(py_jobs)}")
    print("Printing all Python jobs:\n")

    # this loop will extract the contents of the <a> tag (href) and then return
    # it so you can click on the link to apply
    print("PYTHON JOBS:")
    for py_job in py_jobs:
        link = py_job.find('a')['href']
        print(py_job.text.strip())
        print(f"Apply here: {link}\n", end='\n')
        print("-" * 75,'\n' )

def entry_jobs(results):
    ent_jobs = results.find_all('h2',
                                   string=lambda text: 'entry' in text.lower() or 'junior' in text.lower() or 'jr' in text.lower())

    #this loop will extract the contents of the <a> tag (href) and then return
    #it so you can click on the link to apply
    print(f"Available Entry-level Jobs: {len(ent_jobs)}")
    print("Printing all entry-level jobs:\n")

    for job in ent_jobs:
        link = job.find('a')['href']
        print(job.text.strip())
        print(f"Apply here: {link}\n")
        print("-" * 75,'\n' )
