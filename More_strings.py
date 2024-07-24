# .startswith() = creates list of names that start with 'J'

people = ["Johy", "Saray", "Jmily", "Jichael", "Daviy"]
j_team = []
for i in people:
    if i.lower().startswith('j'):
        j_team.append(i)
print(j_team)  # ['John', 'Jmily', 'Jichael']

# .endswith() = creates list of names that end with 'y'
y_team = []
for i in people:
    if i.lower().endswith('y'):
        y_team.append(i)

print(y_team)  # ['Saray', 'Daviy']

# .isalpha() = checks if all characters in a string are alphabetic
letters = 'fsdfsdfgg'
print(letters.isalpha())
# .isdigit() = checks if all characters in a string are digits
nums = "152156341"
print(nums.isdigit())

# .isspace() = Booleen value that checks if all characters in a string is only whitespace spicifically

spaces = "                "

print(spaces.isspace())   #Returns true cause all space

# .split() = splits your string based ona a specific character, default split is on spaces

words = "This-is-one-big-string with many words"
words_list = words.split()
print(words_list)  
words_list = words.split('-')
print(words_list)  # ['This', 'is', 'one', 'big','string

flavors = input("Tell me all your favorite flavors (seperated by a space please): ").split()  # By default will split with a space 
print(flavors)


words_2 = "This-is-one-big-string with many words"
words_list_2 = words_2.split('-')
print(words_list_2)  # ['This', 'is', 'one', '