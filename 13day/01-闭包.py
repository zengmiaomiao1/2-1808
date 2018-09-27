'''
def test(num):
	def test1(x):
		print(x+num)
	return test1
laowang = test(10)
laowang(10)
'''


def line1(a,b):
	def line2(x):
		y = a*x + b
		return y
	return line2
line2 = line1(4,5)
ret = line2(10)
print(ret)
ret1 = line2(20)
print(ret1)



























