# day17 - generators and iterators
# traversing collection such as lists, tuples, or dictionaries

# defining a list
numbers = [1, 2, 3, 4, 5, 6, 7, 2, 2]

# getting a repetition from the list
numbers_repeating = iter(numbers)

# using __next__() method to access elements
print(next(numbers_repeating))
print(next(numbers_repeating))
