import re
class Indeed():

    def parser(soup):
        # Finds job title
        job_title = soup.find_all(class_="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title")
        for job in job_title:
            print(job.text)
        
        company_title = soup.find_all(class_="icl-u-lg-mr--sm icl-u-xs-mr--xs")
        for company in company_title:
            print(company.text)

class Linkedin():
    def parser(soup):
        # Finds job title

        jobcard = []
        job_title = soup.find_all('h1', class_="top-card-layout__title topcard__title")

        for job in job_title:
            # Gives str
            job = job.text
            jobcard.append(job)

        # Finds company
        company_title = soup.find_all('a', class_="topcard__org-name-link topcard__flavor--black-link")

        for company in company_title:
            # Gives str
            company = company.text.lstrip().rstrip()
            jobcard.append(company)

        # Finds country
        country_title = soup.find_all('span', class_="sub-nav-cta__meta-text")

        for country in country_title:
            # Splits the location from "Istanbul, Turkey" to a list
            location = country.text
            jobcard.append(location)
            
        print(jobcard[0],jobcard[1],jobcard[2])

class LinkedinJobCard():
    # Defined the object as title, company, location
    def __init__(self, title, company, location, link):
        self.title = title
        self.company = company
        self.location = location
        self.link = link
    
    # Helps define a repr method for printing job object
    def __repr__(self):
        return "Job Title: " + str(self.title) + "; Company: " + str(self.company) + "; Location: " + str(self.location) + "; Link: " + str(self.link)

class LinkedinSearch():
    
    def parser(soup):

        jobcards = soup.find_all('div', class_="base-card base-card--link base-search-card base-search-card--link job-search-card")

        if len(jobcards) == 0:
            print("No matching jobs found.")
        #
        # class_="base-search-card__info"
        # job_titles = soup.find_all('span', class_="screen-reader-text")

        # for jobbies in job_titles:
        #     jobbies = jobbies.text.lstrip().rstrip()

        # company_titles = soup.find_all('a', class_="hidden-nested-link")

        # for compies in company_titles:
        #     compies = compies.text.lstrip().rstrip()
        jobs = []
        for card in jobcards:
            
            link = card.find('a', class_="base-card__full-link")['href']
            # links = card.find_all('a')
            # for a in links:
            #     card.append(a)
            
            card = card.text
            card = card.split("\n")
            card = [i for i in card if i.strip()]
            k = []

            for i in card:
                j = i.lstrip()
                k.append(j)

            k = k[1:4]
            k.append(link)

            jobs.append(LinkedinJobCard(k[0],k[1],k[2],k[3]))

        return jobs

