# 2 ways to check if a list is emptygit

l = [1]

if (len(l) < 1):
    print ("List is empty")
else:
    print ("List is not empty")

if not l:
    print ("List is also empty this way")
else:
    print ("List is also not empty this way")