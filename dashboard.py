from twitter_pull import pull_stories, stories
from twitter_pull import TwitterStory

f = open("feed/feed.txt", "w")

pull_stories("FoxNews")
pull_stories("CNN")

for x in stories:
    if x.name == "CNN" and x.time[-10] == "3":
        TwitterStory.display_story(x)
        TwitterStory.write_story(x, f)
    else:
        TwitterStory.display_story(x)
        TwitterStory.write_story(x, f)
