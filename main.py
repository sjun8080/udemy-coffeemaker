
def is_resource_sufficient(order_ingredients):
    """Checks if there are enough resources to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

def print_the_report():
    """Prints the current resource values."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")  # Assuming you track money separately

def basic_coffeemachine_operation():
    """Main function to run the coffee machine operation."""
    total_money = 0  # Initialize total money in the machine

    while True:
        prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if prompt == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif prompt == "report":
            print_the_report()  # Assuming this function displays resource details
        elif prompt in MENU:
            drink = MENU[prompt]
            drink_cost = drink["cost"]

            # Check if there are sufficient resources to make the drink
            if is_resource_sufficient(drink["ingredients"]):
                # Process the coin transaction
                money_received = process_coins(drink_cost)

                # If money is successfully received and enough for the drink
                if money_received >= drink_cost:
                    # Deduct resources and update total money in the machine
                    make_coffee(prompt, drink["ingredients"])
                    total_money += drink_cost  # Add the price to total money in the machine
                    print(f"Profit: ${total_money:.2f}")
            else:
                print("Sorry, we don't have enough resources to make this drink.")
        else:
            print("Invalid input. Please choose from espresso, latte, or cappuccino.")



def process_coins(drink_cost):
    """Prompts the user to insert coins and checks if enough money is inserted."""
    print("Please insert coins:")

    try:
        quarter = int(input("How many quarters? "))  # 25 cents
        dime = int(input("How many dimes? "))  # 10 cents
        nickel = int(input("How many nickels? "))  # 5 cents
        penny = int(input("How many pennies? "))  # 1 cent
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0  # Exit the function if input is invalid

    total_money_received = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    print(f"Total money received: ${total_money_received}")

    if total_money_received < drink_cost:
        print("Sorry, not enough money. Refunded")
        return 0
    elif total_money_received > drink_cost:
        change = total_money - drink_cost
        print(f"Here is your change: ${change}")
    else:
        print("Exact amount received. No change needed.")
    return total_money_received



basic_coffeemachine_operation()


"""def process_coins():
    if is_resource_sufficient(drink["ingredients"]): #go ahead receive coins
        print("Please insert coins")


        quarter = input ("How many quaters you want to put in?")
        dime = input("How many dimes you want to put in?")
        nickel = input("How many nickels you want to put in?")
        penny = input("How many pennies you want to put in?")

        quarter_amount = int(quater * 25)
        dime_amount = int(dime * 10)
        nickel_amount = int (nickel * 5)
        penny_amount = int(penny * 1)

        total_money_received = quarter_amount + dime_amount + nickel_amount + penny_amount / 100
        print (f"{total_money_received} has been received")

        price = MENU[prompt]['cost']

        change = int(price - total_money_received)
        print (f"Here you go change {change}")""" #DO NOT MODOFY THIS LINE THIS IS ONE EXAMPLE
