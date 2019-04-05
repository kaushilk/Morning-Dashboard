from twitter_pull import pull_stories, stories


pull_stories("FoxNews")
pull_stories("CNN")


print(stories[0].display_story())
print("\n")
print(stories[-1].display_story())
print(len(stories))

c = 0
f = 0
for x in stories:
    if x.name == "CNN" and x.time[-10] == "5":
        c += 1
        print(x.name)
        print(x.time)
    else:
        f += 1
        print("FOX:", x.time)


print("CNN: ", c)
print("FOX: ", f)
