class person():
	def __init__(self,name):
		self.name = name
		self.__mimi = "	我处过十个对象"#私有方法
		self.__sifangqian = 100
	def getmi(self):#公有方法
		return self.__mimi
	def getmoney(self):
		return self.__sifangqian
ls = person("老宋")
print(ls.getmi())
print(ls.getmoney())

 





















