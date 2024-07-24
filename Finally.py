#finally : this block gets executed regardless of whether an exception was raised or not

groceries = ['apple','banana','pear', 'bread']
while True:
    try:
        item = input("Which item you wanna remove?   ")
        groceries.remove(item)
    except ValueError:
        print(f"No such item '{item}' in the grocery list.")
    except:
        print("Invalid")
    else:  #Runs only if the try block is sucessful
        print(f"Item '{item}' removed successfully")
        break
    finally:
        print("Your current list")
        for item in groceries:
            print(item)
