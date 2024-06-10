import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}


'''
def amazon_scrap(book="", author="", publisher=""):
    products = {'site': 'flipkart', 'items': 0, 'name': [], 'price':[], 'desc':[], 'link': []}
    route = "https://www.amazon.in/s?k="
    response = requests.get(route, headers = HEADERS)

    if response.status_code != 200:
        return None
    
    return None
'''      

def flipkart_scrap(book="", author="", publisher=""):
    products = {'site': 'flipkart', 'items': 0, 'name': [], 'price':[], 'desc':[], 'link': []}

    route = "https://www.flipkart.com/search?q="+book+"books"
    response = requests.get(route, headers = HEADERS)

    if response.status_code != 200:
        return None
        
    
    soup = BeautifulSoup(response.content, "lxml")

    lst = soup.find_all('div', attrs = {'class': 'slAVV4'})
    for prod in lst:
        try:
            name = prod.find('a', attrs = {'class': 'wjcEIp'}).text.strip()
            price = prod.find('div', attrs = {'class': 'Nx9bqj'}).text.strip()
            desc = prod.find('div', attrs = {'class': 'NqpwHC'}).text.strip()
            link = prod.find('a').get('href').strip()
            
            products['name'].append(name)
            products['price'].append(price)
            products['desc'].append(desc)
            products['link'].append(link)
        except:
            pass
    products['items'] = len(lst)
    return products
    



    
    