
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def get_input(prompt, input_type=str, validation=lambda x: True):
    while True:
        try:
            user_input = input_type(input(prompt))
            if validation(user_input):
                return user_input
            else:
                print("Invalid input.")
        except ValueError:
            print("Input must be of type", input_type.__name__)

def customer_name():
    return get_input("Please enter your name: ")

def delivery_details():
    return get_input("Please enter your delivery address: ")

def phone_number():
    return get_input("Please enter your phone number (must be 7 digits): ", int, lambda x: x > 999999 and x < 10000000)

def pizza_list():
    num_pizzas = get_input('How many pizzas would you like (max of 5): ', int, lambda x: 0 < x <= 5)
    selected_pizzas = {'premium': [], 'gourmet': []}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = get_input('Select Your Premium Pizza (or type "next" to finish selecting): ')
        if selected.lower() == 'next':
            break
        selected_pizzas['premium'].append(premium_pizzas[int(selected) - 1])

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = get_input('Select Your Gourmet Pizza (or type "next" to finish selecting): ')
        if selected.lower() == 'next':
            break
        selected_pizzas['gourmet'].append(gourmet_pizzas[int(selected) - 1])

    return selected_pizzas

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizzas_ordered = pizza_list()

    print(f"\nOrder Summary for {name}:")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")
    print("Ordered Pizzas:")
    print(f"Premium: {pizzas_ordered['premium']}")
    print(f"Gourmet: {pizzas_ordered['gourmet']}")

if __name__ == "__main__":
    main()
