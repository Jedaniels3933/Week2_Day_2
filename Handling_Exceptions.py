#try : allows us to try a code block that will potentially raise an exception

# except : in an event that we do run into an exception, we use this block to handle the exception w/o terminating the program

try:
    x = 1
    print(x + 'person')
except:
    print("Hey, we can't actualy do that")

#Specific Exceptions : we can specify the type of exception we are looking for

try:
    div = int(input("Give me a number to divide 10 by: "))
    quotient = 10 / div
    print(f"10 divided by {div} equals {quotient}")
except ValueError:
    print("That's not a valid number. Please enter a whole number.")
except ZeroDivisionError:
    print("You can't divide by zero. Please enter a non-zero number.")
except:
    print("An unexpected error occurred.")

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
               
    
    #finally : this block gets executed regardless of whether an exception was raised or not


