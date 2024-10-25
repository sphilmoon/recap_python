# Get RNA sequence from user
sequence = input("Enter the RNA sequence (for example, AUGCGUACAUCG): ").upper()

# Initialize counters for each nucleotide
count_A = 0
count_U = 0
count_G = 0
count_C = 0

# Repeat over the sequence and count each nucleotide
for nucleotide in sequence:
    if nucleotide == 'A':
        count_A += 1
    elif nucleotide == 'U':
        count_U += 1
    elif nucleotide == 'G':
        count_G += 1
    elif nucleotide == 'C':
        count_C += 1

# Print the result
print(f"A: {count_A}, U: {count_U}, G: {count_G}, C: {count_C}")