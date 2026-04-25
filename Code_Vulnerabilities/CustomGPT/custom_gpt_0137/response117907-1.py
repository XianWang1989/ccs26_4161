
# Example dictionary containing element weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "lithium": 6.94,
    "beryllium": 9.0122,
    "boron": 10.81
    # Add more elements as needed
}

choice = int(input("Enter your choice (1 for elements input): "))

if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))

    elements = []  # List to store user inputs

    for i in range(noelemen):
        element = input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store element in the list

    total_weight = 0.0  # Initialize total weight

    for ele in elements:
        weight = elemen_data.get(ele)  # Get weight from dictionary
        if weight is not None:
            total_weight += weight  # Sum weights
        else:
            print(f"Element '{ele}' not found.")

    print("Total mass =", total_weight)
