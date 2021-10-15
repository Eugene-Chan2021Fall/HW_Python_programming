'''
defining a decorator, calling the function three times

'''
def tripler(my_function):
    def wrap_1():
		def wrap_2():
		def wrap_3():
			 my_function()
		 return wrap_3
		return wrap_2
    return wrap_1

def my_function():
    print("Hello World")
    
