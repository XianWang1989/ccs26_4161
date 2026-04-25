
# Assuming elemen_data is already defined in your code
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(raw_input("Enter 1 for elements: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0  # Initialize total weight variable

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ").lower()
        weight = float(elemen_data.get(element, 0))  # Default to 0 if not found
        total_weight += weight  # Increment the total weight

    print "Total mass =", total_weight
