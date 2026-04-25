
# Example dictionary for element weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    # Add more elements as needed
}

# Function to calculate total mass based on user inputs
def calculate_total_mass():
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0.0
    elements = []

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store elements in a list

    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found in data.")

    print("Total mass =", total_weight)

# Example call to the function
calculate_total_mass()
