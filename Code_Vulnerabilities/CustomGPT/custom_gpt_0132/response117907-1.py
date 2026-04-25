
# Assuming elemen_data is already defined as a dictionary
elemen_data = {"hydrogen": 1.008, "helium": 4.002602}  # Example data

if choice == 1:
    noelemen = int(raw_input("Enter total amount of elements: "))
    elements = []

    # Collect inputs dynamically
    for i in range(noelemen):
        element = raw_input(f"Enter element {i + 1}: ")
        elements.append(element.lower())

    total_weight = 0

    # Calculate total weight
    for element in elements:
        weight = float(elemen_data.get(element))
        if weight is not None:
            total_weight += weight

    print("Total mass =", total_weight)
