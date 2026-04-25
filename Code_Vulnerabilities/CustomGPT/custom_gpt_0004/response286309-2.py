
if __name__ == "__main__":
    obj1 = MyClass()
    obj1.data = [1, 2, 3]

    # Create a deepcopy
    obj2 = copy.deepcopy(obj1)

    # Modify the original
    obj1.data.append(4)

    print("Original:", obj1.data)  # Output: Original: [1, 2, 3, 4]
    print("Deep Copy:", obj2.data)  # Output: Deep Copy: [1, 2, 3]
