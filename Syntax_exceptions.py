
# Syntax Error

#In Python there are 2 issues that will break your code or stop it from executing and throw an error. These are called syntax errors and logical errors.

#Syntax Error: A syntax error occurs when the Python interpreter encounters a statement that is syntactically incorrect. For example, if you forget a closing parenthesis, a comma, or a colon.

#Exceptions - arise when code is structured correctly but produces an error. Python uses try-except blocks to handle exceptions.

#Value error - occurs when a function receives an argument of the correct type but an inappropriate value
str_name = 'nine'
int_num = int(str_num)

#Type error - occurs when a function receives an argument of the correct type but an inappropriate type

num = 5
total_people = num + "people"  # CAnt concatenate a string with an int

#Attribute error - occurs when a variable does not have an attribute

word = "Hello"
word.append("there") # This will throw an AttributeError Can not append to a string

word = "Hello"
rword = word.reversed() # This will throw an AttributeError reversed() is a built-in method, not a string method
