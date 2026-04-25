
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

# Initialize variables
pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00,
              "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}
customer_name = ""
delivery_address = ""
phone_number = ""

def get_customer_name():
    global customer_name
    while customer_name == "":
        customer_name = input("Please enter your name: ")
        if customer_name.isdigit():
            print("Error: Name cannot be a number!")
            customer_name = ""

def get_delivery_address():
    global delivery_address
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")

def get_phone_number():
    global phone_number
    while not phone_number.isdigit() or len(phone_number) < 7:
        phone_number = input("Please enter your phone number (at least 7 digits): ")
        if not phone_number.isdigit():
            print("Phone number must be numeric only!")

def get_num_pizzas():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input("How many pizzas would you like (max of 5): "))
        except ValueError:
            print("Invalid Input. Please enter a number.")
    return num_pizzas

def pizza_selection(num_pizzas):
    for pizza_category, pizzas in [("Premium", premium_pizzas), ("Gourmet", gourmet_pizzas)]:
        print(f'\n=={pizza_category} Pizzas==\n')
        for i, pizza in enumerate(pizzas, start=1):
            print(f'{i}. {pizza}')

        for _ in range(num_pizzas):
            selected = input(f'Select Your {pizza_category} Pizza (or enter "next" to skip): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if selected <= 0 or selected > len(pizzas):
                    print('Invalid Input')
                else:
                    if pizza_category == "Premium":
                        pizza_dict['num_premium_pizzas'] += 1
                    else:
                        pizza_dict['num_gourmet_pizzas'] += 1
            except ValueError:
                print('Invalid Input')

def main():
    get_customer_name()
    get_delivery_address()
    get_phone_number()

    num_pizzas = get_num_pizzas()
    pizza_selection(num_pizzas)

    # Print final receipt details
    print(f'\nReceipt:\nName: {customer_name}\nAddress: {delivery_address}\nPhone: {phone_number}')
    print(f'Total number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
    print(f'Total number of gourmet pizzas: {pizza_dict["num_gourmet_pizzas"]}')
    cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price'] +
            pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print(f'Total cost: {cost:.2f}')

if __name__ == "__main__":
    main()
