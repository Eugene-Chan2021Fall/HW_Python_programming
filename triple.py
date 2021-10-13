#defining a decorator
def tripler(function):
    def wrap_1():
    	def wrap_2():
	    def wrap_3():
        	 function()
    return wrap_1

def my_function():
    print("Hello World")
    
