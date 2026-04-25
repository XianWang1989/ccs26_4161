
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.isalpha():  # Check if the input is not a number
                raise ValueError("Name must be alphabetical.")
            return name  # Return name to proceed
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if not address:  # Ensure not empty
                raise ValueError("Address cannot be empty.")
            return address  # Return address to proceed
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if phone < 1000000:  # Example check for phone number length
                raise ValueError("Phone number must be at least 7 digits.")
            return phone  # Return phone number to proceed
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 0:
                raise ValueError("Number of pizzas cannot be negative.")
        except ValueError as e:
            print(e)

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00,
                  "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for category in ["premium", "gourmet"]:
        while num_pizzas > 0:
            try:
                selected = input(f'Select Your {category.capitalize()} Pizza (enter "next" to finish): ')
                if selected.lower() == 'next':
                    break
                selected = int(selected)
                if selected < 1 or selected > (len(premium_pizzas) if category == "premium" else len(gourmet_pizzas)):
                    raise ValueError("Invalid selection.")
                if category == "premium":
                    pizza_dict['num_premium_pizzas'] += 1
                else:
                    pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
            except ValueError as e:
                print(e)

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizzas = pizza_list()

    print(f"\nName: {name}\nAddress: {address}\nPhone: {phone}")
    print(f"Total Premium Pizzas: {pizzas['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizzas['num_gourmet_pizzas']}")

if __name__ == "__main__":
    main()
