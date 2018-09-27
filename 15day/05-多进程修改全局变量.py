import os
import time
num = 0
pid = os.fork()
if pid == 0:
	print("子进程",num)
else:
	time.sleep(1)
	num+=1
	print("父进程",num)
