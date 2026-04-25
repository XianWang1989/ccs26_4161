
# Define a dictionary with element data
elemen_data = {'hydrogen': 1.008, 'helium': 4.0026, 'lithium': 6.94}  # Add more as needed

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    total_weight = 0

    elements = []
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    # Calculate total weight
    for ele in elements:
        weight = float(elemen_data.get(ele))

        if weight is not None:
            total_weight += weight
        else:
            print(f"Element '{ele}' not found in data.")

    print("Total mass =", total_weight)
