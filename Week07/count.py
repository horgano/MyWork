FILENAME = "count.txt"

def read_number():
    with open (FILENAME) as f:
        number = int(f.read())
        return number

# num = read_number()
# print (num)

def write_number(number):
    with open (FILENAME, "wt") as f:
        f.write(str(number))

# write_number(3)

num = read_number()
num += 1
print (f"we have run the program {num} times")
#write_number(num)