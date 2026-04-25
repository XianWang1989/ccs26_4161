
# Example element data for weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94
}

# Function to get total weight based on user input
def get_total_weight():
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0.0
    elements = []  # List to store elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element in the list

    for element in elements:
        weight = float(elemen_data.get(element, 0))  # Get weight, default to 0 if not found
        total_weight += weight

    print "Total mass =", total_weight

# Usage
if __name__ == "__main__":
    choice = int(raw_input("Choose 1 to calculate total weight: "))
    if choice == 1:
        get_total_weight()
