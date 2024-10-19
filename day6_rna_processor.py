# day 7 using while loop for processing RNA sample. 
# also, using try-except block. 

# Initialize a counter for the sample number.
sample_number = 1

# Loop to process samples
while True:
    # Input validation for total_reads and good_reads
    while True:
        try:
            total_reads = int(input(f"Enter the total number of reads for Sample {sample_number}: "))
            good_reads = int(input(f"Enter the number of good reads for Sample {sample_number}: "))

            # Ensure good_reads is not greater than total_reads
            if good_reads > total_reads:
                raise ValueError("Good reads cannot exceed total reads. Please try again.")

            break  # Exit the loop when input is valid

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid integers for reads.")

    # Calculate percentage of good reads
    percentage_good = (good_reads / total_reads) * 100

    # Print the result
    print(f"Sample {sample_number}: {percentage_good:.2f}% good reads")

    # Input validation for yes/no response
    while True:
        another_sample = str(input("Do you want to process another sample? (y/n): ").lower())

        if another_sample == 'y' or another_sample == 'yes':
            break  # Continue to the next sample
        elif another_sample == 'n' or another_sample == 'no':
            print("Exiting program. Thank you!")
            exit()  # Exit the program if user says 'no'
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    # Increment the sample number
    sample_number += 1