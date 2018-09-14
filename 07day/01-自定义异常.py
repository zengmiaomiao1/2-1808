class show(Exception):
	def __init__(self,name):
		super().__init__()
		self.name = name
		self.error = "input %d is error"%(self.name)
try:
	name = input("请输入一个名字")
	if name == "老王":
		raise showError(name)
except showError as ret:
	print(ret.error)
