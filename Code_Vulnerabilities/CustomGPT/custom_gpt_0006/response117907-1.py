
# Example dictionary for element weights
elemen_data = {
    'hydrogen': 1.00784,
    'helium': 4.002602,
    'lithium': 6.941
}

if __name__ == "__main__":
    choice = int(input("Enter 1 for element input: "))

    if choice == 1:
        noelemen = int(input("Enter total amount of elements: "))

        total_weight = 0
        elements = []  # List to store the elements

        for i in range(noelemen):
            element = input(f"Enter element {i + 1}: ")
            elements.append(element.lower())  # Store each element in the list

            # Look for the weight of the entered element
            weight = float(elemen_data.get(element.lower(), 0))  # Default to 0 if not found

            total_weight += weight  # Sum the weights

        print("Total mass =", total_weight)
