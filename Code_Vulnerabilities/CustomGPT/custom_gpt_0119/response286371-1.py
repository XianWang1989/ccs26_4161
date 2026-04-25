
premium_pizzas = [
    "Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme",
    "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(f"Error: {e}")

    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except:
            print("Error: You must enter something!")

    return delivery_address

def phone_number():
    number = -1
    while number < 0 or len(str(number)) < 7:
        try:
            number = int(input("Please enter your phone number (digits only): "))
        except ValueError:
            print("Error: Phone number must be an integer.")

    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input.')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (enter number): '))
        pizza_dict['num_premium_pizzas'] += 1  # Increment premium pizza count

    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (enter number): '))
        pizza_dict['num_gourmet_pizzas'] += 1  # Increment gourmet pizza count

def main():
    name = customer_name()
    address = delivery_details()
    number = phone_number()
    pizza_list()

    # Print final receipt info
    print(f"\nName: {name}\nAddress: {address}\nPhone: {number}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")
    cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + \
           (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print(f'Total cost: {cost:.2f}')

if __name__ == "__main__":
    main()
