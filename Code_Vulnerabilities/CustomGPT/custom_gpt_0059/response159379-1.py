
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return hash(id(self))  # or another appropriate hash for your use case

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # Output: False
print(hash(obj1))    # Outputs the hash value of obj1
