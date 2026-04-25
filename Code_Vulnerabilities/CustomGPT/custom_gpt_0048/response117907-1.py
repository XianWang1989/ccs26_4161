
# Sample element data dictionary for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # add more elements as needed
}

# Function to get element weights
def get_total_weight(num_elements):
    elements = []

    # Gather inputs
    for i in range(num_elements):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store input in lowercase for consistency

    # Calculate total weight
    total_weight = 0
    for e in elements:
        weight = elemen_data.get(e)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Warning: {e} not found in data.")

    print("Total mass =", total_weight)

# Main logic
choice = int(raw_input("Enter 1 to input elements: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    get_total_weight(noelemen)
