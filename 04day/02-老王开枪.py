class person():
	def __init__(self,name):
		self.name = name
		self.hp = 100
	def NaQiang(self,gun):
		self.gun = gun
	def KaiQiang(self,person):
		zd = self.gun.dj.popzd()
		zd.kill(person)
	def DiaoXue(self,count):
		self.hp -= count
		print(self.hp)
		if self.hp <= 0:
			print("死了%d"%self.hp)
class Gun():
	def __init__(self,name):
		self.name = name
	def zhuangdanjia(self,dj):
		self.dj = dj
class DanJia():
	def __init__(self):
		self.list = []
	def zhuangzidan(self,zd):
		self.list.append(zd)
	def popzd(self):
		return self.list.pop()
class ZiDan():
	def __init__(self):
		self.k = 5
	def kill(self,person):
		person.DiaoXue(self.k)
lw = person("老王")
ak47 = Gun("ak47")
dj = DanJia()
for i in range(30):
	zd = ZiDan()
	dj.zhuangzidan(zd)
ak47.zhuangdanjia(dj)
ls = person("老宋")
lw.NaQiang(ak47)
for i in range(30):
	lw.KaiQiang(ls)
















