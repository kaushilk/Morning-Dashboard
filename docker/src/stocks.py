
from yahoo_fin import stock_info as si

y = open("feed/stock.txt", "w")
# y.write(str(time))
def pull_stock_price(stock):
    return si.get_live_price(stock)

gainers = si.get_day_gainers()
for x in gainers:
    # y.write(x)
    print(x['2'])
    for y in x[0]:
        print(y)













# import requests
# from bs4 import BeautifulSoup
#
# def pull_finance(x):
#     b = open("feeed.txt", "w")
#     source = requests.get('https://finance.yahoo.com/' + str(x))
#     soup = BeautifulSoup(source.text, 'html.parser')
#     list = soup.find_all('td')
#     print(list[0].next_element.next_element.next_element.next_element.next_element.next_element)
#     for tag in list:
#         if tag.string == None:
#             pass
#         else:
#             print(tag)
#             print("\n--------\n")
#             b.write("\n")
#             b.write(tag.string)
#             b.write("\n")
# pull_finance("most-active")
