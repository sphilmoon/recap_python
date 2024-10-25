# day 11 using list and lambda functions
# List of RNA sample quality percentages
rna_quality = [92.5, 88.3, 95.1, 80.0, 99.4]

# 1. Use map() to increase each quality by 5%
increased_quality = list(map(lambda q: q * 1.05, rna_quality))
print(f"Quality after 5% increase: {increased_quality}")

# 2. Use filter() to keep only the high-quality samples (>90)
high_quality = list(filter(lambda q: q > 90, increased_quality))
print(f"High-quality samples (>90): {high_quality}")

# 3. Use sorted() to sort the samples in descending order
sorted_quality = sorted(high_quality, reverse=True)
print(f"Sorted high-quality samples: {sorted_quality}")