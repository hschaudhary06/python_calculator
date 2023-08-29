print("==================\nWelcome\nDear\nUser!\n=================")
print("It's Calculator made in Python !")
print("-----------------")

def calculator():

	try:
		operation = input(''' Please type in the math operation you would like to complete :
                                + for addition
                                - for substraction
                                * for multiplication
                                / for division
                                ** for power
                                % for modulo
                                : ''')
		num1 = int(input("Enter your first number : "))
		num2 = int(input("Enter your second number : "))


		if operation == '+':
			print(f'{num1} + {num2} = ',(num1+num2))
		elif operation == '-':
			print(f'{num1} - {num2} = ',(num1-num2))
		elif operation == '*':
                        print(f'{num1} * {num2} = ',(num1*num2))
		elif operation == '/':
			if num2 != 0:
             			print(f'{num1} / {num2} = ',(num1/num2))
			else:
             			raise ZeroDivisionError("Cannot divide by zero")
		elif operation == '%':
			if num2 != 0:
                              print(f'{num1} % {num2} = ', (num1%num2))
			else:
				raise ValueError("Cannot perform modulo by zero as divisor")
		elif operation == '**':
			print('{num1} ^ {num2} = ',(num1**num2))
		else:
			print("Please Enter valid operation!")
	except ValueError:
		print("Invalid input! please enter valid number.")
	except ZeroDivisionError:
		print("Cannot Divide by Zero")
	except EOFError:
		print("Bye")

calculator()

def again():
	responce = input(''' Do you want to calculate again ? 
		  if yes then Type 'Y' or no then Type 'N' :
		''')
	if responce.upper() == 'Y':
		calculator()
		again()
	elif responce.upper() == 'N':
		print("see you again :).")
	else:
		again()
again()
