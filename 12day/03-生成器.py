def fib():
	a,b = 0,1
	for i in range(10):
		#print(b)
		print("1111111111111111111")
		var = yield b
		print(var)
		print("2222222222222222222")
		a,b = b,a+b
b = fib()
print(b)
#print(next(b))
#print(b.__next__())
print(b.send(None))




































