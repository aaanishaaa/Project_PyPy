MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUES = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}

def is_transaction_success(payment, drink_cost):
    global money
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        print(f"Here is ${change} in change")
        money += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

def is_resources_sufficient(order_ing):
    for item in order_ing:
        if order_ing[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!")

def process_coins():
    print("Please insert coins.")
    total = float(input("How many quarters? ")) * COIN_VALUES["quarter"]
    total += float(input("How many dimes? ")) * COIN_VALUES["dime"]
    total += float(input("How many nickels? ")) * COIN_VALUES["nickel"]
    total += float(input("How many pennies? ")) * COIN_VALUES["penny"]
    return total

is_on = True
money = 0

while is_on: 
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU.get(choice)
        if drink:
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_success(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid selection. Please choose a valid option.")
