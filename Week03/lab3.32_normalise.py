# normalise.py
# Author Niall Horgan

# Program reads in string and strips 
# any leading or trailing spaces 
# It then converts all letters to lower case
# Finally it outputs length of initial string 
# followed by length of stripped string

raw_string = input("Enter a string: ")
stripped_and_lowered = raw_string.strip().lower()

length_raw = len(raw_string)
length_sal = len(stripped_and_lowered)

print (f'Length of \"{raw_string}\" is: {length_raw}')
print (f'By stripping we reduced length of string from {length_raw} to {length_sal}')
print (f'\"{stripped_and_lowered}\"')
