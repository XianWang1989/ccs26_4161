
# Sample element data (just for demonstration)
elemen_data = {
    'hydrogen': 1.008,
    'carbon': 12.011,
    'oxygen': 15.999,
    # Add more elements as needed
}

# Function to get user input for elements
def get_elements(num_elements):
    elements = []
    for i in range(num_elements):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())
    return elements

choice = int(raw_input("Choose an option (1): "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = get_elements(noelemen)

    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
