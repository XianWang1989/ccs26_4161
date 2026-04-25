
# Sample data for elements and their weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    "beryllium": 9.0122,
}

# Get the number of elements from the user
choice = int(input("Enter 1 to continue: "))
if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))

    # Initialize an empty list to hold the elements
    elements = []

    # Gather the elements based on user input
    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    # Calculate the total weight
    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in the data.")

    print("Total mass =", total_weight)
