class Animal():
	def eat(self):
		print("吃")
class Cat(Animal):
	def eat(self):
		print("吃老鼠")
class Dog(Animal):
	def eat(self):
		print("吃骨头")
def common_eat(animal):
	animal.eat()
dog = Dog()
cat = Cat()
common_eat(dog)
common_eat(cat)
























