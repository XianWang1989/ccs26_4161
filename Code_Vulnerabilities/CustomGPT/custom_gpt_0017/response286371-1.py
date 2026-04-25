
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def input_customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.isalpha():  # Ensure name does not contain numbers
            return customer_name
        else:
            print("Error: Name must not contain numbers. Please try again.")

def input_delivery_address():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        else:
            print("Error: Address must not be empty. Please try again.")

def input_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) >= 7:  # Check that there are at least 7 digits
                return phone_number
            else:
                print("Phone number must have at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer. Please try again.")

def input_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 1 <= num_pizzas <= 5:
                return num_pizzas
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

def select_pizzas(num_pizzas):
    for _ in range(num_pizzas):
        print('\n==Premium Pizzas==\n')
        for i, pizza in enumerate(premium_pizzas, start=1):
            print(f"{i}. {pizza}")

        selected = int(input("Select Your Premium Pizza (or enter 0 to skip): "))
        if selected > 0 and selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

        # Repeat for gourmet pizzas
        print('\n==Gourmet Pizzas==\n')
        for i, pizza in enumerate(gourmet_pizzas, start=1):
            print(f"{i}. {pizza}")

        selected = int(input("Select Your Gourmet Pizza (or enter 0 to skip): "))
        if selected > 0 and selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

def main():
    customer_name = input_customer_name()
    delivery_address = input_delivery_address()
    phone_number = input_phone_number()

    num_pizzas = input_num_pizzas()
    select_pizzas(num_pizzas)

    print(f"\nReceipt for {customer_name}:")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")
    total_cost = (pizza_dict['num_premium_pizzas'] * pizza_dict['premium_pizza_price'] +
                  pizza_dict['num_gourmet_pizzas'] * pizza_dict['gourmet_pizza_price'])
    print(f'Total cost: {total_cost:.2f}')

if __name__ == "__main__":
    main()
