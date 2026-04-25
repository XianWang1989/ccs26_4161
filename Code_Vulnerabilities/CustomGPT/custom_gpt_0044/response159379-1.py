
#!/usr/bin/python3

class MyClass(object):    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return False  # Adjust your equality logic as needed
        return NotImplemented

    def __hash__(self):
        # Return a hash value (you might want to define how to hash your instance)
        return hash(id(self))

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 == obj2)  # Output: False
    print(hash(obj1))    # Hash of obj1
