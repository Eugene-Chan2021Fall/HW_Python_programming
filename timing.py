'''
calculating time library to carry out a timing event when a function is finishing running
'''

import time

def calculate_time(func):
    def inner():
        seconds=time.time()
        
        print("Total time "+str(time.time()))
        
    return inner

