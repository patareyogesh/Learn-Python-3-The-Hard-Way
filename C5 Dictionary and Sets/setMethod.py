# creating empty set 
b = set()
# print(type(b))

# adding value to an empty set 
b.add(1)
b.add(2)
b.add(3)
# b.add(2) # u canot add repetetive element 
# b.add([1, 2, 3, 4]) # u canot add list element 
# b.add({1, 2, 3, 4}) # u canot add Dictionary element 
# b.add((1, 2, 3, 4)) # u canot add tuple element 
print(b)

# Length of set 
print(len(b)) # print length of set

# remove elemernt 
b.remove(2) # remove 2 
# b.remove(12) # throwe error 12 not in set
print(b)

# pop
print(b.pop())
print(b)