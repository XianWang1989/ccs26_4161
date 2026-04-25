
def calculate_area(radius):
    """Calculate the area of a circle."""
    return 3.14 * radius ** 2

def calculate_perimeter(radius):
    """Calculate the perimeter of a circle."""
    return 2 * 3.14 * radius

def main():
    r = 5
    area = calculate_area(r)
    perimeter = calculate_perimeter(r)
    print(f"Area: {area}, Perimeter: {perimeter}")

if __name__ == "__main__":
    main()
