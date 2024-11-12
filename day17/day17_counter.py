class CountDown:
	def __init__(self, start):
		self.current = start 

	def __iter__(self):
		return self 

	def __next__(self):
		if self.current <= 0:
			raise StopIteration
		current = self.current
		self.current -= 1 
		return current

# use the custom iterator 
countdown = CountDown(5)
for num in countdown:
	print(num)

def countdown(start):
	while start > 0: 
		yield start
		start -= 1 

# use the generator 
for num in countdown:
	print(num)
