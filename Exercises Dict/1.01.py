# sort dict by normal and reverse
import operator 
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Dict = {key:value}, following sorts bys value automatically
sorted_d = sorted(d.items(), key = lambda x:x[1])
rev_sorted = sorted(d.items(), key = lambda x:x[1], reverse=True) 

# Returns Dict based on key
#sorted_d = sorted(d.items(), key=operator.itemgetter(0))
#rev_sorted = sorted(d.items(), key=operator.itemgetter(0),reverse=True)

print (f"Original dict: {d}")
print (f"Sorted dict: {dict(sorted_d)}")
print (f"Reverse Sorted dict: {dict(rev_sorted)}")