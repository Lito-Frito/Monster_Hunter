import requests
from bs4 import BeautifulSoup
from textwrap import dedent

def find_me_jobs():

    # language = input(dedent("""\
    #     Enter a language to search jobs (e.g. Java or java) or leave blank to see
    #     all developer jobs in your area and press ENTER: """)).replace(' ', '-')
    #
    # location = input(dedent("""
    #     Enter City, State abbreviation (Chicago, IL)to search for jobs or leave
    #     blank and press ENTER: """ )).replace(' ', '-').replace(',', '__2C')

    language = "python"
    location = "Framingham__2C-MA"

    if language:
        #Language and location
        if location:
            URL = dedent(f"""\
            https://www.monster.com/jobs/search/?q={language}&where={location}&st
            page=1&page=3
            """).replace("\n", "")

        #Only language
        else:
            URL = dedent(f"""
            https://www.monster.com/jobs/search/?q={language}&stpage=1&page=3"""
            ).replace("\n", "")

    #if only location
    elif location:
        URL = dedent(f"""\
        https://www.monster.com/jobs/search/?q=Software-Developer&where={location}
        &stpage=1&page=3""").replace("\n", "")

    #if nothing
    else:
        URL = dedent(f"""https://www.monster.com/jobs/search/?q=Software-Developer""")

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')
    job_elems = results.find_all('section', class_='card-content')


    print("\n", end='')

    counter = 0

    def count_n_load_jobs(jobs, counter):
        # this will compile all viable jobs


        for job_elem in job_elems:
            company_elem = job_elem.find('div', class_='company')
            counter += 1

            if None in job_elem:
                counter -= 1
        print(counter)
        input("test")
            # title_elem = job_elem.find('h2', class_='title', string=lambda text: f'{language}' in text.lower())
            # company_elem = job_elem.find('div', class_='company')
            # location_elem = job_elem.find('div', class_='location')
            # link = job_elem.find('a')
            #
            # # #monster has a Section html element that DOESN"T have info, so without this,
            # # #it'll return an error with the print statements afterwards
            # if None in (title_elem, company_elem, location_elem, link):
            #     counter -= 1
            #     continue

        print(f"Search results loaded. {counter} found.")
        input("Press ENTER to print results:")
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
            print(f"Apply here: {link['href']}")
            print(f"Age: {age.text.strip()}\n")
            print("-" * 75,'\n' )

    count_n_load_jobs(job_elems, 0)
    return

find_me_jobs()
