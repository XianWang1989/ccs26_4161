
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False  # Customize your equality logic here

    def __hash__(self):
        return 0  # Customize your hash logic here

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # This will return False
