class Cat():
	def __init__(self):
		print("init")
		self.name = "tom"
		self.money = 1000
	def __str__(self):
		print("str")
		return "str"
	def __del__(self):
		print("del")
	def __new__(cls):#new先执行 创建对象/实例的作用
		return super().__new__(cls)
cat = Cat()#自动调用init new
print(cat.name)

	
