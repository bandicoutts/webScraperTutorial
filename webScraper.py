from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#item-container contains all the relevant information

myURL = 'https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611'

def main():
    uClient = uReq(myURL)
    results = uClient.read()
    uClient.close()
    pageSoup = soup(results, "html.parser")
    containers = pageSoup.findAll("div", {"class":"item-container"})
    