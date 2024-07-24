#Weekend project help:
#Last nights homework
#Calc App

from operations import addition, subtraction , multiplication, division, exponents

def main():
    while True:
        action = input('''
Select an action you'd like to perform:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponents 
6. Quit
'''     )

        if action == '1':
            addition()
        elif action == '2':
            subtraction()
        elif action == '3':
            multiplication()
        elif action == '4':
            division()
        elif action == '5':
            exponents()
        elif action == '6':
            break

main()
