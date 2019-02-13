from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#item-container contains all the relevant information
# will take name of product, price

myURL = 'https://www.newegg.com/Desktop-Memory/SubCategory/ID-147?Tid=7611'

def main():
    uClient = uReq(myURL)
    results = uClient.read()
    uClient.close()
    pageSoup = soup(results, "html.parser")
    containers = pageSoup.findAll("div", {"class":"item-container"})

    for i in containers:
        titleContainer = i.findAll("a", {"class": "item-title"})
        productName = titleContainer[0].text
        titlePrice = i.findAll("li", {"class": "price-current"})
        productPrice = titlePrice[0].text.strip()

        print(productName, productPrice)



main()