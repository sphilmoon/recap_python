# generator expression
squares = (x**2 for x in range(5))

# using the generator
for square in squares:
	print(square)
