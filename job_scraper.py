import requests
from bs4 import BeautifulSoup

language = input("What language do you want to search jobs for or leave blank and press ENTER: ")
location = input("What city OR state do you want to search for jobs or leave blank and press ENTER: ").replace(' ', '-')

if language:

    #Language and location
    if location:
        URL = f'https://www.monster.com/jobs/search/?q={language}&where={location}&stpage=1&page=3'

    #Only language
    else:
        URL = f'https://www.monster.com/jobs/search/?q={language}&stpage=1&page=3'

#if only location
elif location:
    URL = f'https://www.monster.com/jobs/search/?where={location}&stpage=1&page=3'

#if nothing
else:
    URL = f'https://www.monster.com/jobs/search/?q=Software-Developer'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')


print("\n", end='')
print("*" * 75, "\n")
input(f"{len(job_elems)} total search results loaded. \nPress ENTER to print results:")


#Return results of job search
print("Printing jobs:")
# this will print every job posting as text
for job_elem in job_elems:
    # each job_elem is a new BeautifulSoup object
    # you can use the same methods on it as you did before
    title_elem = job_elem.find('h2', class_='title', string=lambda text: f'{language}' in text.lower())
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    link = job_elem.find('a')

    #monster has a Section html element that DOESN"T have info, so without this,
    #it'll return an error with the print statements afterwards
    if None in (title_elem, company_elem, location_elem, link):
        continue

    # elem.text returns only text from that element, not all the HTML tag info
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(f"{location_elem.text.strip()}")
    print(f"Apply here: {link['href']}\n")

    print("-" * 75,'\n' )

#string= searches for an EXACT match, so we use lower() to change all H2 text
#to lowercase, so we can better search, removing the possiblity of some titles
#being in upper case; it also only returns text/discards things like <a> links
#python_jobs = results.find_all('h2',
                               # string=lambda text: 'python' in text.lower())



# #this loop will extract the contents of the <a> tag (href) and then return
# #it so you can click on the link to apply
# print("JOBS:")
# for p_job in job_elems:
#     link = p_job.find('a')['href']
#     print(p_job.text.strip())
#     print(f"Apply here: {link}\n")
#     print("-" * 75,'\n' )

# entry_jobs = results.find_all('h2',
#                                string=lambda text: 'entry' in text.lower() or 'junior' in text.lower() or 'jr' in text.lower())

#this loop will extract the contents of the <a> tag (href) and then return
#it so you can click on the link to apply
# print("ENTRY JOBS:")
# for job in apply_links:
#     link = job.find('a')['href']
#     print(job.text.strip())
#     print(f"Apply here: {link}\n")
#     print("-" * 75,'\n' )

# #THIS IS PYTHON SPECIFIC: FIGURE OUT HOW TO MAKE IT BROAD
# print(f"Available Python Jobs: {len(python_jobs)}")
# print(f"Available Entry-level Jobs: {len(entry_jobs)}")
