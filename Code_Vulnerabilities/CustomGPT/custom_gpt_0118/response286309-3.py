
original = MyClass(42)
original.new_attr = "Hello"

# Specify options for deepcopy
options = {'include': ['value']}

# Perform deepcopy
copied = copy.deepcopy(original, options=options)

# Check values
print(copied.value)     # Outputs: 42
print(copied.new_attr)  # Outputs: AttributeError, since it's not included
