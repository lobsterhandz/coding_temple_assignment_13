import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

# Define keywords for each category
keywords = {
    "Electronics": ["Smartphone", "screen", "memory"],
    "Apparel": ["Cotton", "t-shirt", "size"],
    "Home & Kitchen": ["Stainless steel", "kitchen", "knife"]
}

# Function to tag each product based on keywords
def tag_products(descriptions, keywords):
    tagged_products = []
    for description in descriptions:
        tagged = False
        for category, words in keywords.items():
            for word in words:
                if re.search(rf"\b{word}\b", description, re.IGNORECASE):
                    tagged_products.append((description, category))
                    tagged = True
                    break
            if tagged:
                break
        if not tagged:
            tagged_products.append((description, "Uncategorized"))
    return tagged_products

# Tag the products
tagged_products = tag_products(descriptions, keywords)

# Print the results
for description, tag in tagged_products:
    print(f"Description: '{description}' -> Tag: {tag}")
