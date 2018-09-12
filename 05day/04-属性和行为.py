class Person():
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def eat(self):
		print("吃")
	def sleep(self):
		print("睡觉")
class Bin(Person):
	def look(self):
		print("看电影")
class Xy(Person):
	def music(self):
		print("听音乐")
bin = Bin("斌哥",30)
xy = Xy("小源",27)
bin.eat()
bin.sleep()
bin.look()
xy.eat()
xy.sleep()
xy.music()







