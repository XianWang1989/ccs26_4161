
# Sample element data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    # Add more elements as needed
}

choice = 1  # Assuming this is set based on user choice

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if element not found
        total_weight += weight

    print("Total mass =", total_weight)
