with open ("test3.txt", "w") as f:
    data = f.write("start off")
    print (data)

with open ("test3.txt", "a") as f:
    data = f.write("\nanother line")
    print (data)