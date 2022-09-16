myDict = {
    "Fast" : "in a Quick Manner",
    "Arohi" : "a Girl",
    "Marks" : [1, 2, 5],
    "anotherDict" : {"Yogesh":"a Coder"},
    1 : 22
}
print(myDict.keys()) # print Keys
print(myDict.values()) # print values
print(type(myDict.keys())) # <class 'dict_keys'> Type of dict
print(list(myDict.keys())) # convert into the list 
print(myDict.items()) # print as it is 

print(myDict)
updateDict = {
    "ash" : "freind",
    "Arohi" : "a playerr" # U cannot add duble its update the key value
} 
myDict.update(updateDict) # add key value pair
print(myDict)

print(myDict.get("Arohi"))
print(myDict["Arohi"])

# Differance between .get() and [] syntax
print(myDict.get("Arohi2")) # return non
print(myDict["Arohi2"]) # throwe error not key present 