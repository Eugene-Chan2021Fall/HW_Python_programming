def parse_input():
    input1 = input("Enter value_1: ")
    input2 = input("Enter value_2: ")
    input3 = input("Enter an operator (+,-,*,/,//,**): ")
    return(calculator(input1,input2,input3))


def calculator(num_1, num_2, optr):
    if optr == "+":
        total = num_1 + num_2
        return total

    if optr == "-":
        total = num_1 - num_2
        return total
    if optr == "*":
        total = num_1 * num_2
        return total
    if optr == "/":
	if (num_2==0):
		return false
        total = num_1 / num_2
        return total

    if optr == "//":
        total = int(num_1 / num_2)
        return total

    if optr == "**":
        total = num_1 ** num_2
        return total

    
