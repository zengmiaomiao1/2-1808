class Dog(object):
	__instance = None
	__flag = True
	def __init__(self,name):
		if Dog.__flag:
			self.name = name
			Dog.__flag = False
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
dog = Dog("小红")
dog1 = Dog("小明")
print(id(dog))
print(id(dog1))
print(dog.name)
print(dog1.name)

























