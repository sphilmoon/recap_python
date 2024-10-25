# day 9 of using a list (mutable) 
# List of RNA sample names
rna_samples = ["Sample_001", "Sample_002", "Sample_003", "Sample_004"]

# Corresponding quality percentages for each sample
quality_percentages = [95.5, 89.0, 78.3, 82.1]

# Loop through the samples and print each sample with its quality
for i in range(len(rna_samples)):
    print(f"{rna_samples[i]} has {quality_percentages[i]}% quality")