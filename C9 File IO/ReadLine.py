f = open('D:\Work\C9\sample.txt') 

# Read 1 line
data = f.readline()
print(data)

# Read 2 line
data = f.readline()
print(data)

# Read 3 line .......and so on!
data = f.readline()
print(data)
f.close()