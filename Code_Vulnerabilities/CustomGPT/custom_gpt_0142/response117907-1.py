
# Simulated elemental data for demonstration purposes
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

# Function to get user inputs and calculate total weight
def get_elements_and_calculate_weight(noelemen):
    total_weight = 0.0
    elements = []  # List to hold the user input elements

    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())  # Store the element in the list

    # Calculate the total weight based on the elements collected
    for element in elements:
        weight = float(elemen_data.get(element, 0))  # Default to 0 if element not found
        total_weight += weight

    print("Total mass =", total_weight)

# Main code execution
choice = input("Enter your choice: ")

if choice == '1':
    noelemen = int(raw_input("Enter total amount of elements: "))
    get_elements_and_calculate_weight(noelemen)
