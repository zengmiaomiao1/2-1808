class Animal():
	def __init__(self):
		self.__age = 5
	def Age(self):
		return self.__age
	def __getAge(self):
		return 20
	def getAge1(self):
		return self.__getAge()
class Dog(Animal):
	pass
hsq = Dog()
print(hsq.getAge())
print(hsq.getAge1())






















