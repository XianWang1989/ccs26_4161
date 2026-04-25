
#!/usr/bin/python3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Customize equality logic as needed
        return False

    def __hash__(self):
        return hash((self.__class__,))  # Use a tuple or other attributes for hashing

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # This will now work without warnings
