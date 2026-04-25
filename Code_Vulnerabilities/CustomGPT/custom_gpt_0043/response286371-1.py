
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

# Collects user information
def get_user_info():
    phone_number = get_phone_number()
    customer_name = input("Please enter your name: ")
    delivery_details = get_delivery_address()

    return customer_name, phone_number, delivery_details

def get_phone_number():
    phone_number = -1
    while phone_number < 0 or phone_number < 7:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
        except ValueError:
            print("Phone number must be an integer only (No letters).")
    return phone_number

def get_delivery_address():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except ValueError:
            print("Error! You must enter something.")
    return delivery_address

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Select pizzas
    select_pizza(premium_pizzas, 'num_premium_pizzas', num_pizzas)
    select_pizza(gourmet_pizzas, 'num_gourmet_pizzas', num_pizzas)

def select_pizza(pizza_type, pizza_key, num_pizzas):
    while num_pizzas > 0:
        try:
            selected = input(f'Select Your {pizza_key.replace("_", " ").title()} (or type "next" to skip): ')
            if selected == 'next':
                break
            else:
                selected = int(selected)
            if selected <= 0 or selected > len(pizza_type):
                print('Invalid Input')
            else:
                pizza_dict[pizza_key] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

# Main execution flow
customer_name, phone_number, delivery_address = get_user_info()
pizza_list()

# Final receipt
print(f"\nReceipt:\nCustomer Name: {customer_name}\nPhone Number: {phone_number}\nDelivery Address: {delivery_address}")
print(f'Total number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
print(f'Total number of gourmet pizzas: {pizza_dict["num_gourmet_pizzas"]}')
cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price'] +
        pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
print(f'Total cost: {cost}')
