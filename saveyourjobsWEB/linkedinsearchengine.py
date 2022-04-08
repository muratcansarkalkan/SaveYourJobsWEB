from requests import request
import jobportal
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

def engine(query):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

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

    searchsettings = searchsettings+searchfilter[0]
    searchfunc = searchsettings

    if len(searchfunc) > 0:
        link = link+"?"+searchfunc

    try:
        html = urllib.request.urlopen(link, context=ctx).read()
        soup = BeautifulSoup(html,'lxml')
        result = jobportal.LinkedinSearch.parser(soup)

    except:
        result = ("No matching jobs found.")

    return result