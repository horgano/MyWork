# the statement will automatically close 
# the file when it is finished with it

with open ("testb.txt") as f:
    data = f.read()
    print (data)

# the old way of doin this is 
# f = open ("test_a.txt")
# data = f.read()
# print (data)
# f.close()