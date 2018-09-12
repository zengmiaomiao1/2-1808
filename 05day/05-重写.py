import time
class Dog():
	def __init__(self):
		self.age = 10
	def wark(self):
		print("汪汪叫")
class Xtq(Dog):
	def __init__(self):
		self.name = "哮天犬"
		super().__init__()
	def wark(self):
		for i in range(3):
			print("嗷嗷叫")
			time.sleep(1)
		super().wark()
xtq = Xtq()
xtq.wark()
print(xtq.name)





























