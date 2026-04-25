
# Simulating a dictionary of element weights for demo purposes
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

if __name__ == "__main__":
    choice = int(input("Enter 1 for input: "))  # Updated for Python 3

    if choice == 1:
        noelemen = int(input("Enter total amount of elements: "))  # Updated for Python 3

        total_weight = 0  # Initialize total weight
        elements = []  # List to hold user inputs

        for i in range(noelemen):
            element = input(f"Enter element {i + 1}: ")  # Prompt for each element
            elements.append(element)  # Add input to the list

        # Calculate total weight
        for element in elements:
            weight = elemen_data.get(element.lower())
            if weight is not None:
                total_weight += weight
            else:
                print(f"Warning: '{element}' not found in element data.")

        print("Total mass =", total_weight)
