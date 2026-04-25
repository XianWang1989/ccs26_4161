
# Example element weight data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # add more elements as needed
}

# Function to get total weight of entered elements
def get_total_weight(num_elements):
    total_weight = 0
    elements = []

    for i in range(num_elements):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element in list

    for ele in elements:
        weight = elemen_data.get(ele)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element {ele} not found!")

    return total_weight

# Main program
choice = int(raw_input("Enter 1 to calculate total weight of elements: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = get_total_weight(noelemen)
    print("Total mass =", total_weight)
