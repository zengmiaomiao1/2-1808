class Animal():
	def eat(self):
		print("吃")
	def sleep(self):
		print("睡")

class cat(Animal):
	pass
class Dog(Animal):
	pass
tom = cat()
hsq = Dog()
tom.eat()
tom.sleep()
hsq.eat()
hsq.sleep()




















