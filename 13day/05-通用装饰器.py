def foo(fun):
	print("执行了")
	def fib():
		print("正在装饰中")
		fun()
	return fib
@foo
def test1():
	print("哈哈哈")




















