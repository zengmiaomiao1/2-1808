list = []
f = open('data.data','r')
list = eval(f.read())
print(list)
print(type(list))
f.close()
