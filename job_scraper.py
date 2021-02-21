import requests
from bs4 import BeautifulSoup
from textwrap import dedent

def find_me_jobs():
    language = input(dedent("""\
        Enter a language to search jobs (e.g. Java or java) or leave blank to see
        all developer jobs in your area and press ENTER: """)).replace(' ', '-')

    #formatting is based on how Monster uses location
    location = input(dedent("""
        Enter either a City, State, or both (like this: Chicago, IL) to search
        for jobs or leave blank and press ENTER: """ )).replace(' ', '-').replace(',', '__2C')

    # language = "python"
    # location = "Chicago__2C-IL"

    if language:
        #Language and location
        if location:
            URL = dedent(f"""\
            https://www.monster.com/jobs/search/?q={language}&where={location}&rad=50&st
            page=1&page=3
            """).replace("\n", "")

        #Only language
        else:
            URL = dedent(f"""
            https://www.monster.com/jobs/search/?q={language}&rad=50&stpage=1&page=3"""
            ).replace("\n", "")

    #if only location
    elif location:
        URL = dedent(f"""\
        https://www.monster.com/jobs/search/?q=Software-Developer&where={location}
        &rad=50&stpage=1&page=3""").replace("\n", "")

    #if nothing
    else:
        URL = dedent(f"""https://www.monster.com/jobs/search/?q=Software-Developer&rad=50""")

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    job_elems = results.find_all('section', class_='card-content')
    valid_jobs = results.find_all('h2',
                          string=lambda text: f'{language}' in text.lower())
    print("\n", end='')
    print(f"Search results loaded. {len(valid_jobs)} found.")
    input("Press ENTER to print results:")

    def print_job_details(jobs):
        # this will compile all viable jobs
        print("*" * 75, "\n")

        #Return results of job search
        print("Printing jobs:\n")
        # this will print every job posting as text
        for job_elem in job_elems:

            title_elem = job_elem.find('h2', class_='title', string=lambda text: f'{language}' in text.lower())
            company_elem = job_elem.find('div', class_='company')
            location_elem = job_elem.find('div', class_='location')
            age = job_elem.find('time')
            link = job_elem.find('a')

            #monster has a Section html element that DOESN"T have info, so without this,
            #it'll return an error with the print statements afterwards
            if None in (title_elem, company_elem, location_elem, link):
                continue

            print(title_elem.text.strip())
            print(company_elem.text.strip())
            print(f"{location_elem.text.strip()}")
            print(f"Age: {age.text.strip()}")
            print(f"Apply here: {link['href']}\n")
            print("-" * 75,'\n' )

    print_job_details(valid_jobs)
    return

find_me_jobs()
