
# Sample dictionary simulating the weight of elements
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

# Function to get total weight based on user input
def get_total_weight(noelemen):
    total_weight = 0.0
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")

        # Look for the weight of the entered element
        weight = elemen_data.get(element.lower())

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' is not found in the data.")

    print("Total mass =", total_weight)

# User choice and input
choice = int(raw_input("Enter your choice (1 to continue): "))
if choice == 1:
    noelemen = int(raw_input("Enter total number of elements: "))
    get_total_weight(noelemen)
