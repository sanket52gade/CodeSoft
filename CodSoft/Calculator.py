
# *********** Welcome to the calculator ***********

while True:
    user_input = input("Etnter a Mathematical expression:")
    if user_input =='q':
        break
    else:
        operands = user_input.split()

        if len(operands) !=3:
            print('Invalid Input ! Please provide a valid expression')
        else:
            num1 = float(operands[0])
            operator = operands[1]
            num2 = float(operands[0])

            if operator =='+':
                result = num1+num2
            elif operator =='-':
                result = num1 - num2
            elif operator =='*':
                result = num1 * num2
            elif operator =='/':
                result = num1 / num2
            else:
                print("Invalid Operator ! Please use +, -, *, /")
            print("Result :" ,result)