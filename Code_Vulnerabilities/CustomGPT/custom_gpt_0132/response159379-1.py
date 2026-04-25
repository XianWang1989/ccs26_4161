
#!/usr/bin/python3

class MyClass:
    def __eq__(self, other):
        if not isinstance(other, MyClass):
            return NotImplemented
        return False

    def __hash__(self):
        return hash(id(self))  # Or any other appropriate hashing mechanism

# Example usage
if __name__ == "__main__":
    obj1 = MyClass()
    obj2 = MyClass()

    print(obj1 == obj2)  # Outputs: False
    print(hash(obj1))    # Outputs: Hash value
