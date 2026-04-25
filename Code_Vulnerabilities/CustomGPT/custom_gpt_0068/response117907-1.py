
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'oxygen': 15.999,
    'carbon': 12.011,
    'nitrogen': 14.007
}

choice = int(raw_input("Choose an option (1 for entering elements): "))

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    element_weights = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ").lower()  # Get user input for each element
        weight = elemen_data.get(element)  # Look for the weight of the entered element

        if weight is not None:
            element_weights.append(weight)
        else:
            print(f"Element '{element}' not found.")

    # Calculate the total weight
    total_weight = sum(element_weights)
    print("Total mass =", total_weight)
