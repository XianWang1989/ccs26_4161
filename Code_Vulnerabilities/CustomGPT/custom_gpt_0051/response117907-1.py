
# Dictionary with element weights
elemen_data = {
    "hydrogen": 1.00784,
    "helium": 4.002602,
    "lithium": 6.941,
    # Add more elements as needed
}

# Function to get the total weight of elements based on user input
def get_total_weight():
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Collect elements from user input
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")

    print("Total mass =", total_weight)

# Main execution
choice = int(raw_input("Enter your choice (1 to input elements): "))
if choice == 1:
    get_total_weight()
