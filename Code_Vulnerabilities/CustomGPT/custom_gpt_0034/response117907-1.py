
# Assuming elemen_data is a dictionary that contains element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    # Add more elements as needed
}

choice = 1  # Set this based on user input

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []  # List to store user input elements
    total_weight = 0  # Variable to hold the total weight

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Append each element to the list

    # Calculate total weight
    for element in elements:
        weight = float(elemen_data.get(element))
        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
else:
    print("Invalid choice")
