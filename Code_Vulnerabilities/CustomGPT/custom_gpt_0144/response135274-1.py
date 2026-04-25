# Sample string array
str_array = ['12-34-5678-09-PHOTO', '03-21-1234-56-IMAGE', '99-01-2345-67-VIDEO']

# Function to extract numeric value by removing dashes and converting it to an integer
def numeric_part(key):
    # Extract numeric part by removing hyphens
    numeric = ''.join([c for c in key if c.isdigit()])
    # Return as integer so we can sort numerically
    return int(numeric)

# Sort the array first by numeric part, then by alphabetic order
sorted_array = sorted(str_array, key=lambda x: (numeric_part(x), x))

# Print sorted array
print(sorted_array)
