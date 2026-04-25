
# Dictionary to hold the elemental data
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.941,
    # Add more elements as needed
}

if __name__ == "__main__":
    choice = int(raw_input("Enter 1 to input elements: "))

    if choice == 1:
        noelemen = int(raw_input("Enter total amount of elements: "))
        elements = []  # List to store the entered elements

        # Collecting elements based on user input
        for i in range(noelemen):
            element = raw_input(f"Enter element {i + 1}: ")
            elements.append(element.lower())  # Storing lowercase for consistency

        total_weight = 0  # Variable to hold total weight

        # Calculate total weight
        for elem in elements:
            weight = elemen_data.get(elem)
            if weight is not None:
                total_weight += weight
            else:
                print(f"Element '{elem}' not found in data.")

        print("Total mass =", total_weight)
