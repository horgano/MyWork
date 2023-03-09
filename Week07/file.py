

FILENAME = "data.txt"

'''
with open (FILENAME, "wt") as f:
    for data in f:
        # print (data, end"")
        print (data.strip())
        print (data[:-1])
'''
        
with open ("data2.txt", "a") as f:
    f.write ("what the hell\n")
    f.write ("brown cow\n")

    f.seek(0)  # Go back to start of file to print all after pointer
    data = f.read()
    print data

print ("done")