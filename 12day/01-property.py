class Dog():
	def __init__(self):
		self.__age = 0
	@property
	def age(self):#get
		return self.__age
	@age.setter
	def age(self,age):#set
		self.__age = age
dog = Dog()
#dog.setAge
#print(dog.getAge())
dog.age = 10#相当于执行16行
print(dog.age)#相当于执行17行

































