#coding=utf-8
try:
	#open("1.txt","r")
	#1/0
	#print(b)
	#print("老王")
	number = int(input("请输入功能"))
except (isdigit,ValueError,NameError):
	print("出现异常")
except (NameError,FileNotFoundError):
	print("捕获指定异常")
except Exception as ret:
	print("捕获任何异常")
	print(ret)
else:
	print("没有任何异常走的逻辑")
finally:
	print("不管有没有异常都会走")
'''
不是所有得代码都需要加上异常
可能会出现一次才加上捕获
'''

