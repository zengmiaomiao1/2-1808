import time
def check_login(fun):
	def foo():
		x = time.localtime(time.time())
		a = time.strftime("%Y-%m-%d %H:%M:%S",x)
		print(a)
		f = open("1.txt","a")
		f.write(a)
		f.close()
		fun()
	return foo
@check_login
def test():
	print("买了佛冷")
test()






























