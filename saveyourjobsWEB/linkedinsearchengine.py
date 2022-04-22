from requests import request
import jobportal
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def parser(link):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html,'lxml')
    result = jobportal.LinkedinSearch.parser(soup)
    return result

def listoflinks(link, limit):
    links = []
    for number in range(0,limit+5):
        if number % 25 == 0:
            links.append(link+f"&start={number}")
    return links
    
def fullresults(result, limit, fullresult):
    for i in result:
        fullresult.append(i)
        if len(fullresult) == limit:
            break
    return fullresult

def engine(query,location):
    fullresult = []
    # Base job searching link
    link = "https://www.linkedin.com/jobs/search/"

    # The query function
    # Define search filter and search settings
    searchfilter = []
    searchsettings = ""

    # Define query and convert to URL format
    query = urllib.parse.quote(query)

    # If query exists then filter is appended as keywords=query
    if len(query) > 0:
        searchfilter.append("keywords="+query)
    
    location = urllib.parse.quote(location)
    if len(location) > 0:
        searchfilter.append("location="+location)
    
    if len(searchfilter) == 1:
        searchsettings = searchsettings+searchfilter[0]
    else:
        for i in range(0, len(searchfilter)):
            searchsettings = searchsettings+searchfilter[i]+"&"
    
    searchsettings = searchsettings.rstrip("&")

    searchfunc = searchsettings
    
    limit = 40

    if len(searchfunc) > 0:
        link = link+"?"+searchfunc

    links = listoflinks(link,limit)

    for link in links:
        # try:
            result = parser(link)
            fullresult = fullresults(result, limit, fullresult)
        # except:
        #     result = ("No matching jobs found.")

    return fullresult