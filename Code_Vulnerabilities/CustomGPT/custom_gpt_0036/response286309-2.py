
if __name__ == "__main__":
    # Create an instance of CustomObject
    original = CustomObject([1, 2, 3, 4, 5])

    # Perform a deepcopy of the original object
    copied_object = copy.deepcopy(original)

    # Modify the original to show that the copied object is independent
    original.data.append(6)

    print("Original data:", original.data)  # Output: [1, 2, 3, 4, 5, 6]
    print("Copied data:", copied_object.data)  # Output: [1, 2, 3, 4, 5]
