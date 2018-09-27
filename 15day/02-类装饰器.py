class Test():
	def __init__(self,fun):
		self.fun = fun
	def __call__(self):
		print("哈哈")
		self.fun()
@Test
def test1():
	print("test")
test1()#相当于对象()






































