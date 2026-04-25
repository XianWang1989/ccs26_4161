
# Assumed that elemen_data is defined elsewhere
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add other elements as needed
}

choice = 1  # Example choice; adjust as needed

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))

    elements = []
    total_weight = 0.0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element)

        # Look for the weight of the entered element
        weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if not found
        if weight > 0:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)
