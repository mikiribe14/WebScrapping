import bs4
from urllib.request import urlopen

def download_page():
#returns the Banggood offers page
    file=urlopen("https://www.banggood.com/Flashdeals.html")
    page=file.read()
    file.close()
    return page

def searchOffers(page):
#returns a list of products. Every product is a list of his own data
    tree = bs4.BeautifulSoup(page,"lxml")
    list=tree.find("ul","goodlist_1")
    products=list.find_all("li")

    result=[]
    for item in products:
        product=getProductData(item)
        result.append(product)

    return result

def getProductData(prod):
#returns a list with the name, actual price, old price and % of discount of a product
    data=[]
    name=prod.find("span","title")
    data.append(name.text)
    actPrice = prod.find("span","price")
    data.append(float(actPrice.text[3:]))
    oldPrice=prod.find("span","price_old")
    data.append(float(oldPrice.text[3:]))
    discount=prod.find("span","discount")
    data.append(discount.text[:-4])
    return data

def printOffers(offers):
#prints a message to the user explaining the offers
    for offer in offers:
        print("Hey, the product",offer[0],"is now for just", offer[1],
        "$ !!. (It was for ",offer[2],"$ before). It's a dicount of",offer[3],
         "don't you waste it!!!\n")

if __name__=="__main__":
    page = download_page()
    offers=searchOffers(page)
    printOffers(offers)
