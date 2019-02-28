import bs4
from urllib.request import urlopen

def download_page():
#returns a url????? page
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
    single=[]
    name=prod.find("span","title")
    single.append(name.text)

    actPrice = prod.find("span","price")
    single.append(float(actPrice.text[3:]))

    oldPrice=prod.find("span","price_old")
    single.append(float(oldPrice.text[3:]))

    discount=prod.find("span","discount")
    single.append(discount.text)

    return single




'''find all retorna una llista de "arbres", mentre
find retorna un valor("un arbre")!!!!!!! '''

if __name__=="__main__":
    page = download_page()
    offers=searchOffers(page)
    printOffers(offers)
