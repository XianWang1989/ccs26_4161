
# Example dictionary for element weights
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

choice = int(input("Choose an option (1 for input): "))
if choice == 1:
    noelemen = int(input("Enter total amount of elements: "))

    if noelemen <= 0:
        print("The number of elements must be positive.")
    else:
        elements = []
        total_weight = 0

        for i in range(noelemen):
            element = input(f"Enter element {i+1}: ")
            elements.append(element.lower())
            weight = elemen_data.get(element.lower())

            if weight is not None:
                total_weight += weight
            else:
                print(f"Element '{element}' not found in database.")

        print("Total mass =", total_weight)
