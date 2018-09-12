class Dog():
	print("哈哈哈")
	count = 0
	__a = 1000
	def __init__(self):
		self.name = "老王"
		self.__age = 100
		Dog.count +=1
	def eat(self):
		print("吃")
	def __test(self):
		print("私有方法")
	@classmethod
	def getA(cls):
		return cls.count
	@classmethod
	def setA(cls,count):
		cls.count = count
	@classmethod
	def __show(cls):
		print("show")
	@classmethod
	def show(cls):
		cls.__show()
dog = Dog()
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
print(dog.count)
print(Dog.count)
Dog.setA(10)
print(Dog.getA())
print(dog.getA())
Dog.show()
