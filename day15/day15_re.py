# day 15, recapping regular expression.
# 01_search string
# check if a string contanins a specific pattern.
import re

text = "The RNA sample quality is 95%"
pattern = r"\d+"

result = re.search(pattern, text)
if result:
	print("Found a match: ", result.group())
else: 
	print("No match found.")

# 02_list non-overlapping matches.
text = "RNA quality scores are 95, 89, and 78."
pattern = r"\d+"

matches = re.findall(pattern, text)
print("All matches: ", matches)

# 03_replaces the string with a specified pattern. 
text = "RNA quality scores are 95, 89, and 78."
pattern = r"\d+"
replacement = "[score]"

new_text = re.sub(pattern, replacement, text)
print(new_text)