#
#  Try not to ever give a generic except
#consider logging the error and then reraising it

try:
    number = int(input("Enter a number: "))
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    
