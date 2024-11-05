import re

# Sample data with RNA quality information
text = "Sample_001 quality is 95%, Sample_002 quality is 89%, Sample_003 quality is 78%."

# Regex pattern to capture Sample ID and quality percentage
pattern = r"(Sample_\d+).*?(\d+)%"

matches = re.findall(pattern, text)

# Print extracted data
print("Parsed RNA quality data: ")
for sample_id, quality in matches:
	print(f"{sample_id}: {quality}%")