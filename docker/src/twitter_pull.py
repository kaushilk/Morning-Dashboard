import requests
from bs4 import BeautifulSoup

stories = []
class TwitterStory:
    def __init__(self, name, text, time):
        self.name = name
        self.text = text
        self.time = time
    def display_story(self):
        print(self.name)
        print(self.text)
        print(self.time)
        print("\n")
    def write_story(self, x):
        x.write(self.name)
        x.write("---")
        x.write(self.time)
        x.write("\n")
        x.write(self.text)
        x.write("\n")

def pull_stories(x):
    source = requests.get('https://twitter.com/' + str(x))
    soup = BeautifulSoup(source.text, 'html.parser')
    list = soup.find_all(class_ = 'content')

    n = 1
    for item in list:
        name = x
        text = item.p.contents[0]
        time = item.small.a['title']
        story = TwitterStory(name, text, time)
        stories.append(story)
        n += 1
