def check_login(fun):
	def f1():
		print("检查登录")
		fun()
	return f1



@check_login #cz = check_login(cz) 语法糖
def cz():
	print("充值100")
cz()







































