# day 13 handling files.
file = open("output_example.txt", "w")
file.write("Hello, this is a text.\n")
file.write("Writing some texts in Python.")
file.close()

lines = ["First line\n", "Second line\n", "Third line\n"]
file = open("output_lines.txt", "w")
file.writelines(lines)
file.close()

with open("output_lines.txt", "r") as file:
    content = file.read()
    print(content)

# List of RNA sample data
rna_samples = [
    "Sample_001: Quality=95.5, Reads=100000",
    "Sample_002: Quality=89.0, Reads=120000",
    "Sample_003: Quality=78.3, Reads=95000",
    "Sample_004: Quality=82.1, Reads=105000"
]

# Write RNA sample data to a file
with open("rna_samples.txt", "w") as file:
    for sample in rna_samples: 
        file.write(sample + "\n")

print("RNA sample data has been saved to 'rna_samples.txt'.")

# new sample to append the existing file.
new_sample = "Sample_005: Quality=90.2, Reads=122000"

# append new sample to the existing file
with open("rna_sample.txt", "a") as file: 
    file.write(new_sample + "\n")

print("New sample information has been added to 'rna_sample.txt'.")

import os

# check if the file exists before reading
filename = "rna_samples.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        print("RNA Sample Data: ")
        print(file.read())
else:
    print(f"'{filename}' does not exist. Please create the file first before reading it.")
