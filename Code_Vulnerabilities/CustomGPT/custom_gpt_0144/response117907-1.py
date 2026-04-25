# Simulated data for element weights
elemen_data = {
    "hydrogen": 1.008,
    "helium": 4.0026,
    "carbon": 12.011,
    "oxygen": 15.999,
    # Add more elements as needed
}

# Get number of elements from user
noelemen = int(raw_input("Enter total amount of elements: "))

total_weight = 0.0

for i in range(noelemen):
    element = raw_input(f"Enter element #{i+1}: ")
    weight = elemen_data.get(element.lower())
    if weight is not None:
        total_weight += float(weight)
    else:
        print(f"Element '{element}' not found in data.")

print("Total mass =", total_weight)
