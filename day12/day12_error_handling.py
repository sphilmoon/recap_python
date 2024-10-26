# day 12 using try-except block

while True:
    try:
        number = int(input("Enter an integer: "))
        print(f"You entered: {number}")
        break
    except ValueError:
        print("That's not a valid integer. Please enter a correct value.")

# anther way
print("\nUsing else-finally clauses.")
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer. Please enter a correct value.")
else:
    print(f"You entered: {number}")
finally:
    print("End of the program.")

def check_positive_number():
    while True:
        try:
            number = int(input("Enter a positive integer: "))
            if number < 0:
                raise ValueError("Number must be positive")
            return number   
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

# main program
positive_number = check_positive_number() 
print(f"You entered: {positive_number}.")