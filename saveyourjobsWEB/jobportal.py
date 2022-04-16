import re

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

