# day 5 of reveiwing the key concepts. 
# visualizing multiple samples with bar chart and saving the final results to a text format.
# creating an RNA Sequencing Tool for general QC. 

def calculate_gc_content(sequence):
    """Calculate the GC content of an RNA sequence."""
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

try:
    # Ask the user how many samples they want to input
    num_samples = int(input("How many RNA samples would you like to input? "))

    # Store all sample reports in a list
    all_reports = []

    # Process each sample
    for i in range(num_samples):
        print(f"\n--- RNA Sample {i + 1} ---")

        # Collect sample data from the user
        sample_name = input("Enter the RNA sample name: ")
        total_reads = int(input("Enter the total number of reads: "))
        good_reads = int(input("Enter the number of good reads: "))
        low_quality_reads = int(input("Enter the number of low-quality reads: "))
        sequence = input("Enter the RNA sequence (e.g., 'AUGCGGAUC'): ").upper()

        # Validate that the sum of reads is less than or equal to total reads
        if good_reads + low_quality_reads > total_reads:
            print("Error: The sum of good and low-quality reads exceeds the total reads. Please try again.")
            continue  # Skip this sample if invalid

        # Ask for quality thresholds
        high_quality_threshold = float(input("Enter the high-quality threshold (default is 90%): ") or 90)
        low_quality_threshold = float(input("Enter the low-quality threshold (default is 5%): ") or 5)

        # Perform calculations
        percentage_good = (good_reads / total_reads) * 100
        percentage_low_quality = (low_quality_reads / total_reads) * 100
        gc_content = calculate_gc_content(sequence)

        # Create report for the current sample
        report = (
            f"\n--- RNA Sample Quality Report ---\n"
            f"Sample: {sample_name}\n"
            f"Total reads: {total_reads}\n"
            f"Good reads: {good_reads} ({percentage_good:.2f}%)\n"
            f"Low-quality reads: {low_quality_reads} ({percentage_low_quality:.2f}%)\n"
            f"GC Content: {gc_content:.2f}%\n"
        )

        # Determine sample quality
        if percentage_good >= high_quality_threshold and percentage_low_quality <= low_quality_threshold:
            report += "Result: Excellent sample quality!\n"
        elif percentage_good >= high_quality_threshold:
            report += f"Result: Good quality, but too many low-quality reads (> {low_quality_threshold}%).\n"
        else:
            report += "Result: Poor sample quality.\n"

        # Append the report to the list
        all_reports.append(report)

        # Display bar chart visualization
        print("\n--- Bar Chart Visualization ---")
        max_width = 50
        good_reads_bar = int((percentage_good / 100) * max_width)
        low_quality_reads_bar = int((percentage_low_quality / 100) * max_width)

        # Print the bar charts
        print(f"Good reads:    [{'#' * good_reads_bar:<50}] {percentage_good:.2f}%")
        print(f"Low-quality:   [{'#' * low_quality_reads_bar:<50}] {percentage_low_quality:.2f}%")

    # After processing all samples, display and save reports
    if all_reports:
        full_report = "\n".join(all_reports)
        print("\n--- All Sample Reports ---")
        print(full_report)

        with open("rna_qc_reports.txt", "w") as file:
            file.write(full_report)
        print("Reports saved to 'rna_qc_reports.txt'.")

except ValueError:
    print("Error: Invalid input. Please enter numbers where required.")