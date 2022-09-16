letter ='''Dear <|NAME|>, 
Greeting from Yogesh Company. I am happy to tell you about your selection 
You are selected!
Have a great day ahead!
Bill
Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)