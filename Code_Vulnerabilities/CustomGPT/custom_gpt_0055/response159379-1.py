
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False
        return NotImplemented

    def __hash__(self):
        return hash((id(self),))  # or any other logic to generate a hash

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # False
print(hash(obj1))    # Hash value of obj1
print(hash(obj2))    # Hash value of obj2
