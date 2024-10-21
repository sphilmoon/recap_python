# Day 8 using function definitions

# Define a function to calculate the percentage of good reads
def calculate_good_reads_percentage(total_reads, good_reads):
    return (good_reads / total_reads) * 100

# Define a function to decide sample quality
def check_qc(percentage_good, excel_limit=90, good_limit=75):
    if percentage_good >= excel_limit:
        return "Excellent quality!"
    elif percentage_good >= good_limit:
        return "Good quality."
    else:
        return "Bad quality :("

# Define variables to get input from the user
total_reads = int(input("Enter the total number of reads: "))
good_reads = int(input("Enter the number of good reads: "))

# Calculate the percentage of good reads
percentage_good = calculate_good_reads_percentage(total_reads, good_reads)

# Ask if the user wants to use custom limits
use_custom_limit = input("Do you want to use custom QC threshold? (Y/N): ").lower()

if use_custom_limit == 'y' or use_custom_limit == 'yes':
    excel_limit = int(input("Enter the excellent quality threshold: "))
    good_limit = int(input("Enter the good quality threshold: "))
    quality = check_qc(percentage_good, excel_limit, good_limit)
else:
    quality = check_qc(percentage_good)

# Print the result
print(f"Percentage of good reads: {percentage_good:.2f}%")
print(f"Sample quality: {quality}")