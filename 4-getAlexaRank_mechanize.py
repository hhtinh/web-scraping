import mechanize
import cookielib
from bs4 import BeautifulSoup

def changerankscrapper(site):
    """
    Takes a site url, scrapes that site's Alexa page,
    and returns the site's global Alexa rank and the
    change in that rank over the past three months.
    """

    #Create Alexa URL
    url = "http://www.alexa.com/siteinfo/" + site

    #Get HTML
    cj = cookielib.CookieJar()
    mech = mechanize.OpenerFactory().build_opener(mechanize.HTTPCookieProcessor(cj))
    request = mechanize.Request(url)
    response = mech.open(request)
    html = response.read()

    #Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    globalrank = int(soup.find("strong", { "class" : "metrics-data" }).text)
    changerank = int(soup.find("span", { "class" : "change-wrapper change-up" }).text)

    return globalrank, changerank

#Example
site = "vnexpress.net"
globalrank, changerank = changerankscrapper(site)

print(globalrank)
print(changerank)
