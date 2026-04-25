
# Sample element data (replace this with your actual data)
elemen_data = {
    'hydrogen': 1.008,
    'helium': 4.0026,
    'lithium': 6.94,
    # Add more elements as needed
}

if __name__ == "__main__":
    choice = int(input("Enter your choice: "))  # Change to input() for Python 3

    if choice == 1:
        noelemen = int(input("Enter total amount of elements: "))

        total_weight = 0.0
        elements = []

        for i in range(noelemen):
            element = input(f"Enter element {i + 1}: ")
            elements.append(element.lower())

        for elem in elements:
            weight = float(elemen_data.get(elem))
            if weight is not None:
                total_weight += weight
            else:
                print(f"Element {elem} not found.")

        print("Total mass =", total_weight)
