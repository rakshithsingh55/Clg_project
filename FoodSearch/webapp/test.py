# Python3 code to demonstrate working of 
# Common words among tuple strings 
# Using join() + set() + & operator + split() 

# Initializing tuple 
test_tup = ('gfg is best', 'gfg is for geeks', 'gfg is for all') 

# printing original tuple 
print("The original tuple is : " + str(test_tup)) 

# Common words among tuple strings 
# Using join() + set() + & operator + split() 
res = ", ".join(sorted(set(test_tup[0].split()) & set(test_tup[1].split()) & set(test_tup[2].split()))) 

# printing result 
print("Common words among tuple are : " + res) 
