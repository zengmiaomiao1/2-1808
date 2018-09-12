class A():
	def __init__(self):
		self.a = 10
	def test(self):
		print("test")
	def test2(self):
		print("我是A")
class B():
	def __init__(self):
		self.b = 20
	def test1(self):
		print("test1")
	def test2(self):
		print("我是B")
class C(A,B):
	def test3(self):
		print("哈哈")
c = C()
c.test()
c.test1()
print(c.a)
c.test2()
c.test3()
print(C.__mro__)
