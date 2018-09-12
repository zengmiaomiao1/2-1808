class Home():
	def __init__(self,address,area,type):
		self.address = address
		self.area = area
		self.type = type
		self.list = []
	def __str__(self):
		msg = "我家的名字是%s,我的床有%d个"%(self.address,len(self.list))
		return msg
	def ban(self,jiaju):
		all = 0
		for bed in self.list:
			all+=bed.area
		diff = self.area - all
		print("剩余%d"%diff)
		if diff >= jiaju.area:
			self.list.append(jiaju)
		else:
			print("不够了")
class jiaju():
	def __init__(self,area,name):
		self.area = area
		self.name = name
lxl = Home("北京市长安街666号",1500,"八室八厅")
bed = jiaju(50,"席梦思")
for i in range(40):
	lxl.ban(bed)
print(lxl)













