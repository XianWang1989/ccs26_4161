
# Create an instance of MyClass
original = MyClass(10)

# Perform a deep copy
import copy
copied = copy.deepcopy(original)

# Modify the copied instance
copied.value = 20

# Print values to demonstrate they are independent
print("Original value:", original.value)  # Outputs: 10
print("Copied value:", copied.value)      # Outputs: 20
