
# Assuming you have a dictionary with element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

# Function to get element weights
def get_total_weight(num_elements):
    total_weight = 0
    elements = []

    for i in range(num_elements):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

        # Look for the weight of the entered element
        weight = elemen_data.get(element.lower())
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    return total_weight, elements

# Main execution
choice = int(raw_input("Enter your choice (1 to get total mass): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    total_mass, entered_elements = get_total_weight(noelemen)
    print("Total mass =", total_mass)
