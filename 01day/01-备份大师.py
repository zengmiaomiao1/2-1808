f = open("8.txt","r")
content = f.read()
print(content)
f.close()

name = input('请输入备份的文件的名字')
p = name.rfind(".")
s =name[:p]
e = name[p:]
newname = s+'备份'+e
f = open(name,'r')
f = open("newname","w")
while True:
	content = f.read(1024)
	f1.write(content)
	if len(content) == 0:
		break
f1.close()
f.close()





















