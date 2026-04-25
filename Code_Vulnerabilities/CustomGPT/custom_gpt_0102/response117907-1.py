
# Assuming elemen_data is your dictionary with element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    # Add more elements as needed
}

# Function to get total weight of elements
def get_total_weight():
    choice = int(input("Enter 1 for weight calculation: "))
    if choice == 1:
        noelemen = int(input("Enter total amount of elements: "))

        total_weight = 0.0
        elements = []

        for i in range(noelemen):
            element = input(f"Enter element {i + 1}: ")
            elements.append(element.lower())

        for element in elements:
            weight = elemen_data.get(element)
            if weight is not None:
                total_weight += weight
            else:
                print(f"Element '{element}' not found in data.")

        print("Total mass =", total_weight)

# Call the function
get_total_weight()
