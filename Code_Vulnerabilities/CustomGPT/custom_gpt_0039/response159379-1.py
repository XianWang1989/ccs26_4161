
#!/usr/bin/python -3

class MyClass(object):
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return True  # Implement your equality logic here
        return NotImplemented

    def __hash__(self):
        return hash(())  # Provide a suitable hash value based on your attributes

# Example usage
if __name__ == "__main__":
    a = MyClass()
    b = MyClass()
    print(a == b)  # This will now work without warnings
