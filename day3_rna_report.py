# day 4 of python recap: basic input and output

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
        report = (
            f"\n--- RNA Sample Quality Report ---\n"
            f"Sample: {sample_name}\n"
            f"Total reads: {total_reads}\n"
            f"Good reads: {good_reads} ({percentage_good:.2f}%)\n"
            f"Low-quality reads: {low_quality_reads} ({percentage_low_quality:.2f}%)\n"
        )

        # Check quality criteria
        if percentage_good >= high_quality_threshold and percentage_low_quality <= low_quality_threshold:
            report += "Result: Excellent sample quality!\n"
        elif percentage_good >= high_quality_threshold:
            report += f"Result: Good sample quality, but the low-quality reads exceed {low_quality_threshold}%.\n"
        else:
            report += "Result: Poor sample quality.\n"

        print(report)

        # Create a simple text-based bar chart
        print("\n--- Bar Chart Visualization ---")

        # Set max width for the bar
        max_width = 50

        # Normalize the percentages to fit the max width
        good_reads_bar = int((percentage_good / 100) * max_width)
        low_quality_reads_bar = int((percentage_low_quality / 100) * max_width)

        # Print bars
        print(f"Good reads:    [{'#' * good_reads_bar:<50}] {percentage_good:.2f}%")
        print(f"Low-quality:   [{'#' * low_quality_reads_bar:<50}] {percentage_low_quality:.2f}%")

        # Save report to a file
        with open("rna_report.txt", "w") as file:
            file.write(report)
        print("Report saved to rna_report.txt.")
    
except ValueError:
    print("Error: Please enter valid numeric values for the reads.")