
# Define a dictionary with example element data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.002602,
    'lithium': 6.94,
    'beryllium': 9.0122,
    'boron': 10.81,
    'carbon': 12.011,
    # ... add more elements as needed
}

# Simulate user choice (for this example we set it manually)
choice = 1

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    # Initialize a list to store element names
    elements = []

    # Loop to accept user input for each element
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element in list

    # Calculate the total weight
    for elem in elements:
        weight = float(elemen_data.get(elem, 0))  # Use 0 if the element is not found
        total_weight += weight

    print("Total mass =", total_weight)
