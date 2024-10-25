# day 3 recapping python

# arithmetic operations
x = 20
y = 9

print(f"addition: {x+y}")
print(f"subtraction: {x-y}")
print(f"multiplication: {x*y}")
print(f"division: {x/y:2f}")
print(f"floor division: {x//y}")
print(f"modulus: {x%y}") # remainder
print(f"exponentiation: {x**y}")

# comparison operations
a = 22
b = 155

print(f"Is A equal to B? {a == b}")
print(f"Is A not equal to B? {a != b}")
print(f"Is A greater than B? {a > b}")
print(f"Is A less than B? {a < b}")
print(f"Is A greater than or equal to B? {a >= b}")
print(f"Is A less than or equal to B? {a <= b}")

# logical operations
quality_score = 92
is_paired_end = True

if quality_score > 90 and is_paired_end:
    print("This sample meets the high-quality criteria and paired-end sample.")
else:
    print("The sample does not meet the criteria.")

# arithmetic combined
x = 10
x += 5 # x = x+5
print(f"X after adding 5: {x}")

x *= 2 # x = x*2
print(f"X after multiplying by 2: {x}")