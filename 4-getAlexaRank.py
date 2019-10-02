from urllib.request import urlopen
from bs4 import BeautifulSoup

def alexaRanks(site):
    #Create Alexa URL
    url = "http://www.alexa.com/siteinfo/" + site

    #Get HTML
    html = urlopen(url)	
    bsObj = BeautifulSoup(html.read(), "html.parser");
    #print(bsObj)
	
    globalrank = int(bsObj.find("span", { "class" : "globleRank" }).find("strong", { "class" : "metrics-data" }).get_text())

    #changerank = int(bsObj.find("span", { "class" : "change-wrapper" }).get_text())	
    
    localrank = int(bsObj.find("span", { "class" : "countryRank" }).find("strong", { "class" : "metrics-data" }).get_text())

    #return globalrank, changerank, localrank
    return globalrank, localrank
	
site = "http://vnexpress.net"

#globalrank, changerank, localrank = alexaRanks(site)
globalrank, localrank = alexaRanks(site)

print(globalrank)
#print(changerank)
print(localrank)
