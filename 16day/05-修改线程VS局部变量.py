from threading import Thread,current_thread
def run(name):
	num = 0
	for i in range(10):
		num+=1
	print(current_thread().name,num)
t1 = Thread(target = run,args = (current_thread().name,))
t2 = Thread(target = run,args = (current_thread().name,))
t1.start()
t2.start()














































