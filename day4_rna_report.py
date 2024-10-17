# day 4: basic user input and output. 
# using try-excect block for avoiding the program crash and user friendly feedback. 

try:
    # Ask the user for input
    sample_name = input("Enter the RNA sample name: ")
    total_reads = int(input("Enter the total number of reads: "))
    good_reads = int(input("Enter the number of good reads: "))
    low_quality_reads = int(input("Enter the number of low-quality reads: "))

    # Validate the reads
    if good_reads + low_quality_reads > total_reads:
        print("Error: The sum of good and low-quality reads exceeds the total reads.")
    else:
        # Ask for custom thresholds (with defaults)
        high_quality_threshold = float(input("Enter the high-quality threshold (default is 90%): ") or 90)
        low_quality_threshold = float(input("Enter the low-quality threshold (default is 5%): ") or 5)

        # Calculate percentages
        percentage_good = (good_reads / total_reads) * 100
        percentage_low_quality = (low_quality_reads / total_reads) * 100

        # Print a formatted report
        print("\n--- RNA Sample Quality Report ---")
        print(f"Sample: {sample_name}")
        print(f"Total reads: {total_reads}")
        print(f"Good reads: {good_reads} ({percentage_good:.2f}%)")
        print(f"Low-quality reads: {low_quality_reads} ({percentage_low_quality:.2f}%)")

        # Check quality criteria based on user-defined thresholds
        if percentage_good >= high_quality_threshold and percentage_low_quality <= low_quality_threshold:
            print("Result: Excellent sample quality!")
        elif percentage_good >= high_quality_threshold:
            print(f"Result: Good sample quality, but the low-quality reads exceed {low_quality_threshold}%.")
        else:
            print("Result: Poor sample quality.")
    
except ValueError:
    print("Error: Please enter valid numeric values for the reads.")