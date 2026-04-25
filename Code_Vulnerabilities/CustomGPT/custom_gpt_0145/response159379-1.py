
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        # Return a unique hash value; here it's a constant value for demonstration.
        # Adjust this as needed based on your object's attributes.
        return hash((self.__class__,))
