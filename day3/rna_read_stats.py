# define the number of total reads and good reads
total_reads = 229000
good_reads = 214083
low_quality_reads = 12000

# calculate the percentage of good reads and low quality reads
percentage_good_reads = (good_reads / total_reads) * 100
percentage_low_reads = (low_quality_reads / total_reads) * 100

# set a quality threshold
high_quality_threshold = 90
low_quality_threshold = 5

# compare with logical operators to check conditions 
#if percentage_good_reads >= high_quality_threshold:
#    print(f"Excellent quality! Good reads: {percentage_good_reads:.2f}%")
#elif percentage_good_reads < high_quality_threshold >= 90:
#    print(f"Good quality. Good reads: {percentage_good_reads:.2f}%")
#else:
#    print(f"Bad quality. Good reads: {percentage_good_reads:.2f}%")

# check the quality of the reads
if percentage_good_reads >= high_quality_threshold and percentage_low_reads <= low_quality_threshold:
    print(f"Excellent quality! Good reads: {percentage_good_reads:.2f}%, Low-quality reads: {percentage_low_reads:.2f}%")
elif percentage_good_reads >= high_quality_threshold:
    print(f"Good quality. Good reads: {percentage_good_reads:.2f}%, but with a high percentage of low quality reads: {percentage_low_reads:.2f}%")
else:
    print(f"Bad quality. Good reads: {percentage_good_reads:.2f}%")