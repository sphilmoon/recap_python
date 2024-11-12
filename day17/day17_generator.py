# using a generator with 'yield' 
def countdown(start):
	while start > 0: 
		yield start
		start -= 1 

# use the generator 
for num in countdown:
	print(num)
