# day 10 of using dictionary key-value pair.
# Dictionary of RNA samples and their quality percentages
rna_quality = {
    "Sample_001": 95.5,
    "Sample_002": 89.0,
    "Sample_003": 78.3,
    "Sample_004": 82.1
}
    
# Access using square brackets
print(rna_quality["Sample_001"])  # Output: 95.5
# Access using the get() method
print(rna_quality.get("Sample_002"))  # Output: 89.0

# Add a new sample to the dictionary
rna_quality["Sample_005"] = 88.7
print(rna_quality)
# Update the quality of an existing sample
rna_quality["Sample_002"] = 91.0
print(rna_quality)

# Remove a specific sample
del rna_quality["Sample_002"]
print(rna_quality)
# Remove and return 
quality_removed = rna_quality.pop("Sample_003")
print(f"Removed quality: {quality_removed}")
print(rna_quality) 

# Print the quality of each RNA sample
for sample, quality in rna_quality.items():
    print(f"{sample} has a quality of {quality}%")
    
# Check if a sample exist in the dictionary 
if "Sample_005" in rna_quality:
    print("Sample_005 is in the dictionary.")
else:
    print("Sample_005 is NOT in the dictionary.") 
    
# Get all the keys
print(rna_quality.keys()) 
# Get all the values
print(rna_quality.values())
# Update the dictionary with a new sample
rna_quality.update({"Sample_006": 89.9})
print(rna_quality) 

# Access nested dictionary
rna_data = {
    "Sample_001": {"quality": 95.5, "reads": 100000},
    "Sample_002": {"quality": 89.0, "reads": 120000}
}

# Access nested data
print(rna_data["Sample_001"]["quality"])
print(rna_data["Sample_001"]["reads"])
