import requests
from bs4 import BeautifulSoup

language = input("Please enter what language to search jobs for: ")
location = input("Please enter what city OR state you want to search for jobs:").replace(' ', '-')

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
# print(URL)

print("\n", end='')
print("*" * 75, "\n")
print(f"{len(job_elems)} total search results loaded.")




#Filter by role
role = input("Please enter a role to filter results or leave blank:")
print(role)
# if role:
#     jobs_by_role = results.find_all('h2',
#                                string=lambda text: f'{role}' in text.lower())
#
#     for roles in job_elems:
#     title_elem = jobs_by_role.find('h2', class_='title')
#     company_elem = jobs_by_role.find('div', class_='company')
#     location_elem = jobjobs_by_role_elem.find('div', class_='location')
#
#     if None in (title_elem, company_elem, location_elem):
#         continue
#
#     for jobs in jobs_by_role:
#         print(title_elem.text.strip())
#         print(company_elem.text.strip())
#         print(f"{location_elem.text.strip()}", "\n")


# for job in jobs_by_role:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#
#     if None in (title_elem, company_elem, location_elem):
#         continue
#
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(f"{location_elem.text.strip()}", "\n")
#     print("-" * 75,'\n')
#
# print("Printing job-job_elems:")
# #this will print every job posting as text
# for job_elem in job_elems:
#     # each job_elem is a new BeautifulSoup object
#     # you can use the same methods on it as you did before
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#
#     #monster has a Section html element that DOESN"T have info, so without this,
#     #it'll return an error with the print statements afterwards
#     if None in (title_elem, company_elem, location_elem):
#         continue
#
#     # elem.text returns only text from that element, not all the HTML tag info
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(f"{location_elem.text.strip()}", "\n")
#     print("-" * 75,'\n' )
#
# #string= searches for an EXACT match, so we use lower() to change all H2 text
# #to lowercase, so we can better search, removing the possiblity of some titles
# #being in upper case; it also only returns text/discards things like <a> links
# python_jobs = results.find_all('h2',
#                                string=lambda text: 'python' in text.lower())
#
# #this loop will extract the contents of the <a> tag (href) and then return
# #it so you can click on the link to apply
# # print("PYTHON JOBS:")
# # for p_job in python_jobs:
# #     link = p_job.find('a')['href']
# #     print(p_job.text.strip())
# #     print(f"Apply here: {link}\n")
# #     print("-" * 75,'\n' )
#
# entry_jobs = results.find_all('h2',
#                                string=lambda text: 'entry' in text.lower() or 'junior' in text.lower() or 'jr' in text.lower())
#
# #this loop will extract the contents of the <a> tag (href) and then return
# #it so you can click on the link to apply
# print("ENTRY JOBS:")
# for job in entry_jobs:
#     link = job.find('a')['href']
#     print(job.text.strip())
#     print(f"Apply here: {link}\n")
#     print("-" * 75,'\n' )
#
# print(f"Available Python Jobs: {len(python_jobs)}")
# print(f"Available Entry-level Jobs: {len(entry_jobs)}")
