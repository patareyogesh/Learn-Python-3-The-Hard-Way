content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline() 

        if 'python' in content:
            print(content)
            print(f"Yesss Python is present on line no {i}")
        i+=1
            