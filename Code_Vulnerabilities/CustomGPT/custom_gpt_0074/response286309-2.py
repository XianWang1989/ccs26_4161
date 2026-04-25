
original = ExampleClass(value=10)
options = {'update_value': 20}

# Using custom deepcopy method with options
deep_copied_instance = copy.deepcopy(original, options=options)

print(f"Original Value: {original.value}")  # Output: Original Value: 10
print(f"New Value: {deep_copied_instance.value}")  # Output: New Value: 20
