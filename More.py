
#Else: additional code block that will only execute if the try block is sucessfull

while True:
        try:
            age = int(input("Enter your age: "))
            birthday = age + 1
        except ValueError:
            print("That's not a valid number. Please enter a whole number.")
        except:
            print("Invalid response")
        else:
            print(f"On your birthday you will be {birthday} years old!.")
            break