import time

def calculate_time(func):
    def inner(*arg):
        seconds=time.time()
        res = func(*arg)
        print("Total time "+str(time.time()-t))
        return res
    return inner

@calculate_time
def Funct_2(n):
    time.sleep(n)

if __name__ == "__main__":
    Funct_2(2)
