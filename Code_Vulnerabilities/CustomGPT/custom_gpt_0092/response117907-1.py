
# Assuming elemen_data is a dictionary that holds the element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

# Function to get total weight based on user inputs
def get_total_weight(noelemen):
    total_weight = 0
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store input in a list

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"{element} not found in element data.")

    print("Total mass =", total_weight)

# Main code
choice = int(raw_input("Enter 1 to proceed: "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    get_total_weight(noelemen)
