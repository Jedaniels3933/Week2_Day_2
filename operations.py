

def addition():
     while True:
        try:
            a = int(input('Please enter first number for addition:'))
            b = int(input('Please enter second number for addition:'))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"Ooops, unexcepted error: {e}")
        else:
            print(f"The result of adding {a} + {b} is: {a + b}")
            break


def subtraction():
    while True:
        try:
            a = float(input('Please enter first number for sub:'))
            b = float(input('Please enter second number for sub:'))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"Ooops, unexcepted error: {e}")
        else:
            print(f"The result of subtracting {a} - {b} is: {a - b}")
            break  

def division():
    while True:
        try:
            a = float(input('Please enter first number for div:'))
            b = float(input('Please enter second number for div:'))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"Ooops, unexcepted error: {e}")
        else:
            print(f"The result of dividing {a} / {b} is: {round}")
            break   

def multiplication():  
    while True:
        try:
            a = float(input('Please enter first number for Mult:'))
            b = float(input('Please enter second number for mult:'))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"Ooops, unexcepted error: {e}")
        else:
            print(f"The result of mult {a} x {b} is: {a * b}")
            break 


def exponents():
    while True:
        try:
            a = int(input('Please enter first number for the base:'))
            b = int(input('Please enter the number for the power :'))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except Exception as e:
            print(f"Ooops, unexcepted error: {e}")
        else:
            print(f"The result of {a} raised to the power of  {b} is: {a ** b}")
            break
        



