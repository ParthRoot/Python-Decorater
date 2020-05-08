def dict(func1):
	def dis():
		print("Execute Start")
		func1()
		print("Hello Students")
	return dis()

def fun1():
	print("Jane Lya km kar")

#mehtod 1 use decoraters	
fun1()
fun1 = dict(fun1)

#mehtod 2 use decoraters
@dict
def fun2():
	print("print fun2")
fun2()