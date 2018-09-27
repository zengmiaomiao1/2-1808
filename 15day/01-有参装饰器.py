def test0(arg):
	def test3(fun):
		def f1():
			if arg == 1:
				print("验证1")
			elif arg == 2:
				print("验证2")
			fun()
		return f1
	return test3
def test4(fun):
	def f1():
		print("验证2")
		fun()
	return f1


#test3 = test0(1)
@test0(1)
def test1():
	print("test1")#验证1
@test0(2)
def test2():
	print("test2")#验证2
test1()
test2()
