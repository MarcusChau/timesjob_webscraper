# This web scraper is scrapping for python jobs from:
# https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
#                         '=submit&txtKeywords=python&txtLocation='
import time
from bs4 import BeautifulSoup  # import bs4 library
import requests  # import requests
from datetime import datetime  # time library


def find_jobs():
    # using request to get the website
    html_txt = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                            '=submit&txtKeywords=python&txtLocation=').text

    # using Beautifulsoup lib to read the website using lxml
    soup = BeautifulSoup(html_txt, 'lxml')

    # using find all to parse through and specifically find all the jobs
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # looping through all jobs, extracting specific information from each one
    for index, job in enumerate(jobs):
        # finding post day
        post_day = job.find('span', class_='sim-posted').span.text
        # sorting based on 'few' keyword
        if 'few' in post_day:
            # company name
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            # skill set required
            skill_set = job.find('span', class_='srp-skills').text.replace(' ', '')
            # more info
            more_info = job.header.h2.a['href']
            # time now
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open(f'post/{index}.txt', 'a') as f:
                f.write(f"{dt_string}")
                f.write("\n")
                f.write(f"Company name: {company_name.strip()}\n")
                f.write(f"Skill set: {skill_set.strip()}\n")
                f.write(f"Additional information link: {more_info}\n\n")
                print(f"File saved: {index}")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        # Every ten minutes
        time.sleep(time_wait * 60)
