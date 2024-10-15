# Learning python syntax, variables, data types, and type conversion.
# 
# step 1. Print statement
if 12 > 5:
    print("12 is greater than 5.")

# step 2. Variables to store data

# integer (whole number)
read_count = 145000
good_reads = 139000

# float (decimal)
quality_score = 99.8

# string (text)
sample_name = "RNA_SAMPLE_001"

# boolean (true or false value)
is_paired_end = True

# exercise 1. 
print("Sample Name:", sample_name)
print("Read Count:", read_count)
print("Quality Score:", quality_score)
print("Is Paired End:", is_paired_end)

##########################################

quality_name = "Paired-end"
combined_name = sample_name + " - " + quality_name
print(combined_name)

# exercise 2. Performing basic calculations
percentage_good = (good_reads / read_count) * 100 
high_quality = quality_score > 98.0 

print(f"The percentage of good reads: {percentage_good:.2f}%")

if high_quality and is_paired_end:
    print("The sample meets the high quality criteria :)")
else:
    print("The sample DOES NOT meet the quality criteria.")

##########################################

# Converting 'integer' to 'string'
print(f"The read count is {read_count}.")
read_count_str = str(read_count)
print("The read count is " + read_count_str)

# Converting 'string' to 'integer'
reads = "56000"
reads_int = int(reads)
print(f"when you convert str to int, the read count: {reads_int + 22000}")

