
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        return False

    def __hash__(self):
        return hash(id(self))  # Or any hash calculation based on your class attributes

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # This will return False as intended
