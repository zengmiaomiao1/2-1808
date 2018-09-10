class Teacher():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def teach(self):
		print('教书育人')
	def sleep(self):
		print('睡觉')
	def eat(self):
		print('吃')
	def introduce(self):
		print('我叫%s年龄%d'%(self.name,self.age))
	def __str__(self):#当你打印对象的时候,可以描述对象一些信息
		msg = '我叫%s年龄%d'%(self.name,self.age)
		return msg
sy = Teacher('孙院',30)
sy.teach()
sy.sleep()
sy.eat()
print(sy)
