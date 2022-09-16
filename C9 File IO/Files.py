# f = open('D:\Work\C9\sample.txt','r')
f = open('D:\Work\C9\sample.txt') # By Deffault r mode
# f = open('sample.txt','r')
data = f.read()
# data = f.read(5) # Read first 5 characters
print(data)
f.close()