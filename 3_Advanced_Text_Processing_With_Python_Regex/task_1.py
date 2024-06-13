import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

# Define the key you want to extract the value for
key_to_extract = "Occupation"

# Write a regex pattern to extract the value for the specified key
pattern = rf"{key_to_extract}: ([^;]+)"

# Use re.search to find the key and extract its value
match = re.search(pattern, text)

if match:
    value = match.group(1)
    print(f"The value for '{key_to_extract}' is: {value}")
else:
    print(f"No value found for the key '{key_to_extract}'")
