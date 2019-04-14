from twitter_pull import pull_stories, stories
from twitter_pull import TwitterStory
import datetime

time = datetime.datetime.now()
day = str(time.day)[1]

f = open("feed/feed.txt", "w")

pull_stories("FoxNews")
pull_stories("CNN")


print(time, "\n----------")
for x in stories:
    if x.name == "CNN" and x.time[-10] == day:
        TwitterStory.display_story(x)
        TwitterStory.write_story(x, f)
    else:
        TwitterStory.display_story(x)
        TwitterStory.write_story(x, f)
