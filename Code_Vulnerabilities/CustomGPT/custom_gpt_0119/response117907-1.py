
# Dictionary to store element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    # Add more elements as needed
}

# Function to calculate total weight
def calculate_total_weight(noelemen):
    total_weight = 0
    elements = []

    # Collect inputs in a loop
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store in a list for later use

    # Calculate weights for collected elements
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)

# User input for the number of elements
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    calculate_total_weight(noelemen)
