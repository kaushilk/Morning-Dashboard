from twitter_pull import pull_stories, stories

f = open("feed/feed.txt", "w")

pull_stories("FoxNews")
pull_stories("CNN")

for x in stories:
    if x.name == "CNN" and x.time[-10] == "0":
        f.write(x.name)
        f.write("---")
        f.write(x.time)
        f.write("\n")
        f.write(x.text)
        f.write("\n")

    else:
        f.write(x.name)
        f.write("---")
        f.write(x.time)
        f.write("\n")
        f.write(x.text)
        f.write("\n")
