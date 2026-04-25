
# Example data for elements
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Function to handle user input and calculate total weight
def calculate_total_weight():
    choice = int(input("Enter 1 to start: "))  # use input() for Python 3

    if choice == 1:
        noelemen = int(input("Enter total amount of elements: "))

        elements = []
        total_weight = 0

        for i in range(noelemen):
            element = input(f"Enter element {i + 1}: ")
            elements.append(element.lower())

        # Calculate total weight
        for element in elements:
            weight = elemen_data.get(element)
            if weight is not None:
                total_weight += weight
            else:
                print(f"Element '{element}' not found.")

        print("Total mass =", total_weight)

# Run the function
calculate_total_weight()
