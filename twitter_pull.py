import requests
from bs4 import BeautifulSoup

class TwitterStory:
    def __init__(self, name, text, time):
        self.name = name
        self.text = text
        self.time = time

def pull_stories(x):
    source = requests.get('https://twitter.com/' + str(x))
    soup = BeautifulSoup(source.text, 'html.parser')
    list = soup.find_all(class_ = 'content')

    n = 1
    for item in list:
        print("\nCNN Story #", n , "\n------------")
        text = item.p.contents[0]
        time = item.small.a['title']
        print(time, "\n", text, "\n------------")
        n += 1

pull_stories("FoxNews")
