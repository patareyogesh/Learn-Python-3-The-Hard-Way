myDict = {
    "pankha" : "fan",
    "Dabba" : "box",
    "vastu" : "item"

}
print("Option are ", myDict.keys())
a = input("Enter the Marathi Word\n")
# print("The meaning of your word is ", myDict[a])
# When you canot expect any error use this (When use enter another key value )
print("The meaning of your word is ", myDict.get(a))# Return None when key value wrong 