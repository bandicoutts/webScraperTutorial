from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myURL = 'https://www.trademe.co.nz/cool-auctions'

def main():
    uClient = uReq(myURL)
    results = uClient.read()
    uClient.close()
    pageSoup = soup(results, "html.parser")
    containers = pageSoup.findAll("ul", {"class": "list-view-list"}) #picks out cool auctions

    for i in containers:
        pass # will be coming back to this


main()