#Strings
#Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence. For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

# ====   Strings are IMMUTABLE ==== Once created their content can not be changed
#can index into one but can't change them
# 
# You can reassign the var name into a new string but original string remains unchanged

my_string = "Hello World!"
print(id(my_string)) # objects mem access

my_string = "Hello, Python!"
print(id(my_string)) 
print(my_string) #The text changed but string did not change in memory

first_char = my_string[0]
print(first_char)
#Slice it by idex

substring = my_string[0:5]
print(substring) #Prints the word hello index 

# Iterating over strings

for i in my_string:  #lists eash letter vertically
    print(i)

#Formatted Strings
# using .format()
name = "Jeremiah"
formatted_str = "Hello, {}".format(name)
print(formatted_str)  # displays as "Hello, Jeremiah"
formatted_str = f"Hello, {name}"
print(formatted_str)  # displays as "Hello, Jeremiah"

#  Useful string methods
#len function - length of string or iterable
test = "How many CHARACTERS are in this string?"
print(len(test))   # Prints number of chatacts in the string

# .upper():  returns all caps 
print(test.upper())
# .lower()   returns lowercase version of string 
print(test.lower())

#isinstance() - checks if an object is an instance of a class
#  isuper():  return T or F to check All caps v/s lower case

txt = "This is NOW"
print(txt.isupper()) # FALse

#   .title(): returns a title cased version of string, caps every word sep by a space

person = "abraham lincoln"
print(person.title()) # Abraham Lincoln

#-----  .replace(<thing to replace>,<What to replace with >): replace a sub with a new value

txt2 = "I like apples!"
x = txt.replace('apples','bananas')
print(x)  # I like bananas!


# .split(): by default splits each word sep by a space

new_txt2 = ''
words = txt2.split()
print(words)  # ['I', 'like', 'apples!']
for i in words:
    print(i)
    if i == 'bananas':
        new_txt2 += 'oranges '
    else:
        new_txt2 += i

#Learn this , dont forget

# .lstrip() .rstrip() .strip() = allows us to strip whitespace (empty space) out of a string

test = "                                   I feel lost most of the time      "
left_strip = test.lstrip()  #strips away the left white space
print(left_strip)  
right_strip = test.rstrip()  #strips away the right white space
print(right_strip)
strip_both = test.strip()  #strips away both left and right white space
print(strip_both)

# .join() : joins a list of strings into one string
words = ["Let's", "join", "these", "words", "together"]
join = " !".join(words)
print(join)  # let's join these words together- joined them
another_join = "!!!! !!!! ".join(words)
print(another_join)  # let's join these words together- joined them

# .find() : search for a word in a string and return its index[0] 
txt = "Welcome to my world!"
found = txt.find("Welcome")
print(found)  # 0

#   .count() : counts the number of times a word appears in a string

txt = "Foxy Brown is a foxy lady. Is she actually a fox, IDK,  maybe we should as a real fox?"
print(txt.count('fox'))
print(txt.lower().count('fox'))  # counts the number of times 'fox' appears in the string, ignoring case













