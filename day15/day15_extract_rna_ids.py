import re

# sample text containing RNA sample IDs
text = "We analyzed these RNA samples: Sample_001, Sample_002, Sample_003."

# regex pattern to match "Sample_XXX"
pattern = r"Sample_\d+"

# find all matching ids 
sample_ids = re.findall(pattern, text)
print("Extracted sample IDs: ", sample_ids)

# grouping with parentheses
text = "Sample_001 has a quality of 95%"
pattern = r"(Sample_\d+).*?(\d+)%" # look for digits followed by a %

result = re.search(pattern, text)
if result:
	print("Sample ID:", result.group(1))
	print("Quality:", result.group(2) + "%")


# Find samples with "high" quality label
text = "Sample_001_high, Sample_002_low, Sample_003_high"
pattern = r"Sample_\d+(?=_high)"

matches = re.findall(pattern, text)
print("High-quality samples:", matches)  
# Output: ['Sample_001', 'Sample_003']