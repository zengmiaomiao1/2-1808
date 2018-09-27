def foo(fun):
	def f1(*args,**kwargs):
		print("买了佛冷")
		fun(*args,**kwargs)
	return f1
@foo
def test(num):
	print("haha",num)
test(1)




















































