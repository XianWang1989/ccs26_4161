
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Define your equality logic here
        return False

    def __hash__(self):
        return id(self)  # or implement a custom hash logic

# Example usage
obj1 = MyClass()
obj2 = MyClass()

print(obj1 == obj2)  # True
print(hash(obj1))    # Outputs the hash of obj1
