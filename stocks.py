import requests
from bs4 import BeautifulSoup

def pull_finance(x):
    b = open("feeed.txt", "w")
    source = requests.get('https://finance.yahoo.com/' + str(x))
    soup = BeautifulSoup(source.text, 'html.parser')
    list = soup.find_all('td')
    print(list[0].next_element.next_element.next_element.next_element.next_element.next_element)
    for tag in list:
        if tag.string == None:
            pass
        else:
            
            b.write("\n")
            b.write(tag.string)
            b.write("\n")
pull_finance("most-active")





# from yahoo_fin import stock_info as si
#
# print(si.get_live_price("amzn"))
