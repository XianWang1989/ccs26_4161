
# Example element data
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

def get_elements(noelemen):
    elements = []
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())
    return elements

def calculate_total_weight(elements):
    total_weight = 0
    for element in elements:
        weight = elemen_data.get(element)
        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{element}' not found.")
    return total_weight

# Main flow
choice = int(raw_input("Enter 1 to input elements: "))
if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = get_elements(noelemen)
    total_weight = calculate_total_weight(elements)
    print("Total mass =", total_weight)
