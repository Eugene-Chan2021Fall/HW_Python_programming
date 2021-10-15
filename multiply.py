def multiply_list():
    '''
    asking user to enter the a list of integer and multiply each element in there as the question requires 
    '''
    strg_input=input("Enter a list of integers with space between")
    num_list=strg_input.split()
    
    total = 1
    for i in range(len(num_list)):
        num_list[i]=int(num_list[i])
    t1 = [x*(x+1) for x in num_list]
        
    return total    
