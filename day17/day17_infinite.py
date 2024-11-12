def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
