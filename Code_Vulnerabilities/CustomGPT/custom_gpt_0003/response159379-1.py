
#!/usr/bin/python -3

class MyClass(object):    
    def __eq__(self, other):
        # Ensure we are comparing with an instance of MyClass
        if isinstance(other, MyClass):
            return False  # Implement your actual equality logic here
        return NotImplemented

    def __hash__(self):
        # Return a hash value; this can be anything that makes sense for your class
        return id(self)  # Using the object's id as a simplistic hash value

# Example usage
if __name__ == "__main__":
    a = MyClass()
    b = MyClass()
    print(a == b)  # This will print False and won't raise a warning
    print(hash(a))  # Now this works as well since __hash__ is implemented
