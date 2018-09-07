import os
name = input('请输入文件夹名字')
files = os.listdir(name)
print(os.getcwd())
os.chdir(name)#切换路径
print(os.getcwd())#打印路径
for i in files:
	p = i.rfind('.')
	s = i[:p]
	e = i[p:]
	nn = s+"精品"+e
	os.rename(i,name)#重命名











































