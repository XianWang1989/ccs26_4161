
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # or implement your own logic here
        return False

    def __hash__(self):
        return 0  # or some constant value; adjust based on your logic

# Example usage
obj1 = MyClass()
obj2 = MyClass()
print(obj1 == obj2)  # This should return True
