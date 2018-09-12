class Xs():
	def __init__(self):
		self.list = []
		se5lf.read()
		print(self.list)
def save(self):
	d = {}
	name = input("请输入姓名")
	age = input("请输入年龄")
	d["name"] = name
	d["age"] = age
	self.list.append(d)
	self.writelocation()
def writelocation(self):
	f = open("1.data","w")
	f.write(str(self.list))
	f.close()
def read(self):
	f = open("1.data","r")
	self.list = eval(f.read)
	f.close()
sm = Xs()
sm.save()
#def delete(self):
	#pass
#def change(self):
	#pass
#def find(self):
	#pass
#def menu(self):
	#while True:
		#num = int(input("请输入功能1:添加2:查看"))
		#if num == 1:
			#self.insert()
		#elif num == 2:


			#self.find()
'''
def save(self): 
		f.write(str(self.cards))
		if len(f.read())!=0
			print(eval(f.read()))
cm = ca()
cm.menu()
'''









