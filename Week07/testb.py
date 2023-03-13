
with open ("testb.txt", "w") as f:
    data = f.write("\n hello")
    print (data) 

with open ("testb.txt", "w") as f2:
    data = f2.write ("another line\n")
    print (data)

with open ("testb.txt", "r") as f3:
    data = f3.read()
    print (data)