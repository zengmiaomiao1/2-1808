class Dog():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print('吃')
	def sleep(self):
		print('睡觉')
za = Dog('za',8)
za.sleep()
print(za.name)
print(za.age)

