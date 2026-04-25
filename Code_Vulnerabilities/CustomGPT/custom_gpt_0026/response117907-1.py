
# Sample dictionary to store element weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    "beryllium": 9.0122
    # Add more elements as needed
}

# User choice for number of elements
choice = int(input("Enter 1 to input elements: "))  # Use `input` for Python 3
if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))
    elements = []  # List to store the entered elements

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")  # Gather input in a loop
        elements.append(element.lower())  # Store elements in lowercase

    total_weight = 0  # Initialize total weight

    # Calculate total weight
    for elem in elements:
        weight = elemen_data.get(elem)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element {elem} not found in data.")

    print("Total mass =", total_weight)
