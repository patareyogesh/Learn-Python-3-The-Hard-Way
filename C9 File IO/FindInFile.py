with open("log.txt") as f:
    content = f.read().lower() # this help to find captial or missmatches 

if 'python' in content:
    print("Yesss Python is present")
else:
    print("Nooo python is not present")