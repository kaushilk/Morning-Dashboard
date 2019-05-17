from twitter_pull import pull_stories, stories
from twitter_pull import TwitterStory
from to_do import full_name
import datetime
from to_do import projects

time = datetime.datetime.now()
day = str(time.day)[1]

f = open("feed/feed.txt", "w")

f.write(str(time))
f.write("\n----------\n")
f = open("feed/feed.txt", "r")
print(f.read())

pull_stories("FoxNews")
pull_stories("CNN")


print(time, "\n----------")
for x in stories:
    if x.name == "CNN" and x.time[-10] == day:
        # TwitterStory.display_story(x)
        TwitterStory.write_story(x, f)
    else:
        # TwitterStory.display_story(x)
        TwitterStory.write_story(x, f)

<<<<<<< HEAD
print(full_name)
=======
y = open("feed/feed.txt", "r")
print(y.read())
>>>>>>> 0273db1b88be9b63eee93c110b1da7ca15e43af2
