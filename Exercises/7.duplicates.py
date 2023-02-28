


a = [10,20,30,20,10,50,60,40,80,50,40]

unique = []

def check():
    for x in a :
        if x not in unique:
            unique.append(x)
    print (unique)
    
# print (unique)
check()
