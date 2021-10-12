def multiply_list():
    strg_input=input("Enter a list of integers with space between")
    print("\n")
    num_list=strg_input.split()
    for i in range(len(num_list)):
        num_list[i]=int(num_list[i])

    for x in num_list:
        total =  num_list[x]*num_list[x+1]
    return total    
