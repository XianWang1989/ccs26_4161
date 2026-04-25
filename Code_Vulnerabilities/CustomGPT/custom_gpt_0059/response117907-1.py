
# Sample data for demonstration
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# User selects the number of elements
choice = 1  # Assume this is set based on user input
if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))  # Use input() for Python 3

    # Initialize a list to hold the elements
    elements = []

    # Collect the elements from user input
    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store in lowercase for consistency

    # Calculate total weight
    total_weight = 0
    for ele in elements:
        weight = elemen_data.get(ele)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{ele}' not found in data.")

    print("Total mass =", total_weight)
