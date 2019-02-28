import bs4
from urllib.request import urlopen

def download_page():
    file=urlopen("https://www.banggood.com/Flashdeals.html")
    page=file.read()
    file.close()
    '''print(page)'''
    return page

def searchOffers(page):
    tree = bs4.BeautifulSoup(page,"lxml")
    list=tree.find("ul","goodlist_1")
    products=list.find_all("li")

    result=[]
    for item in products:
        thingsList=getOffers(item)
        result.append(thingsList)

    print(result)

def getOffers(prod):
    single=[]
    actPrice = prod.find("span","price")
    single.append(actPrice.text)

    oldPrice=prod.find("span","price_old")
    single.append(oldPrice.text)

    #print(actPrice.text, oldPrice.text)

    return single




'''find all retorna una llista de "arbres", mentre
find retorna un valor("un arbre")!!!!!!! '''

def getOffers2(plist):
    result=[]
    for product in plist:
        result.append()

if __name__=="__main__":
    page = download_page()
    searchOffers(page)
