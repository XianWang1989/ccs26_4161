
# Example dictionary holding element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    'beryllium': 9.0122,
    'boron': 10.81,
    'carbon': 12.011,
    'nitrogen': 14.007,
    'oxygen': 15.999,
    # Add more elements as needed
}

choice = int(input("Enter choice (1 to get total weight): "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    total_weight = 0

    # Loop to get each element input
    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ").lower()  # Get element input
        weight = float(elemen_data.get(element, 0))  # Get weight, default to 0 if not found
        total_weight += weight  # Add to total weight

    print("Total mass =", total_weight)
