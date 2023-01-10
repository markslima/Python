# TODO 1. Print Report ✅
# TODO 2. Check resources sufficient
# TODO 3. Process coins  ✅
# TODO 4. Check transaction successful / add money to tiller (if successful)
# TODO 5. Make coffee / deduct resources


from art import logo
from data import menu

def cls():
    print("\n" * 50)

def beverage(beverage, beverage_ingredients, beverage_cost):
    new_beverage = {}
    new_beverage[menu] = beverage
    new_beverage[menu] = beverage_ingredients
    new_beverage[menu] = beverage_cost
    menu.append(new_beverage)

menu = {
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

PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25
CHANGE = 0


espresso = menu['espresso']['cost']
latte = menu['latte']['cost']
cappuccino = menu['cappuccino']['cost']

# print(f'Latte cost is: ${latte}0')

machine = {
    'water': 300, 
    'milk': 200, 
    'coffee': 100, 
}

cls()
print(logo)

coffee = True
# Espresso
#   50ml Water
#   18g Coffee
#   Cost: $1.50
#
# Latte
#   200ml Water
#   24g Coffee
#   150ml Milk
#   Cost: $2.50
#
# Cappuccino
#   250ml Water
#   24g Coffee
#   10ml Milk
#   Cost: $3.00

def take_order():
    TILLER = 0

    drink = input("\nWhat would you like? ([E]spresso/[L]atte/[C]appuccino): ").lower()
    if drink[0] == 'e':
        print("\nOkay, so you will be having an Espresso.")
        drink = 'espresso'
        drink_cost = espresso
        machine['water'] -= 50

        print(f"Okay, that will be ${espresso}0\n")
    elif drink[0] == 'l':
        print("\nGreat, one Latte coming right up!")
        drink = 'latte'
        drink_cost = latte
        print(f"So that'll be ${latte}0\n")
    elif drink[0] == 'c':
        print("\nWhoa, a Cappuccino sounds fucking delicious right about now.")
        drink = 'cappuccino'
        drink_cost = cappuccino
        print(f"That will cost you ${cappuccino} \n")
    elif drink == 'report':
        for value, key in machine.items():
            print(f"{value}: {key}")
        print(machine)
    elif drink == 'OFF'.lower():
        print("\n***Coffee Machine: Powering Down ***\n")
        return False
    else:
        print(f"\nHmm, sorry, we don't make {drink} at this cafe. Fuck you.")
        return False
        
    # Coin Processing
    print("Please insert coins: ")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    # Confirmation of payment received
    cash = (quarters * QUARTER) + (dimes * DIME) + (nickels * NICKEL) + (pennies * PENNY)
    print(f"\nOkay that's ${round(cash, 2)} in payment")
    
# answer = str(round(answer, 2))

    if cash < drink_cost:
        print(f"That's not enough money.")
    elif cash > drink_cost:
        print(f"Great, here's your {drink} ☕️ ")
        print(f"Your change is: ${round(cash - drink_cost,2)}")
        TILLER +=  drink_cost
        print(f"The till so far: {TILLER}")
    elif cash == drink_cost:
        print(f"Terrific! Just enough money for your {drink} ☕️ ")
        TILLER +=  drink_cost
        print(f"The till so far: {TILLER}")

while coffee:
    take_order()


# program must process coin payment
# print("Please insert coins.")
# print("Sorry, but that's not enough coins. Money refunded.")
# 1) Print Report
# 2) Check for sufficient resources
# 3) Process Coins
# 4) Check transaction
# 5) Make coffee