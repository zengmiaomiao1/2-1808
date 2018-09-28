import threading
import time
class MyThrea1d(threading.Thread):
	def run(self):
		if mutexA.acquire():
			print(self.name+'-----dol----up----')
			time.sleep(1)
			if mutexB.acquire():
				print(self.name+'----dol-----down----')
				mutexB.release()
			mutexA.release()

class MyThread2(threading.Thread):
	def run(self):
		if mutexB.acquire():
			print(self.name+'-----dol----up----')
			time.sleep(1)
			if mutexA.acquire():
				print(self.name+'----dol-----down----')
				mutexA.release()
			mutexB.release()

mutexA = threading.Lock()
mutexB = threading.Lock()









