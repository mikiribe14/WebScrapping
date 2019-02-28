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
    print(list)


if __name__=="__main__":
    page = download_page()
    searchOffers(page)
