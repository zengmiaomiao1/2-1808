class Dog():
	def __str__(self):
		return "哈哈"
	def __init__(self,name):
		self.name = name
	def __del__(self):
		print("啊")
hsq = Dog("哈士奇")
hsq1 = hsq
del hsq
del hsq1
print("哈哈")

































