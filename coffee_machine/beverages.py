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

# def beverage(beverage, beverage_ingredients, beverage_cost):
#     new_beverage = {}
#     new_beverage[menu] = beverage
#     new_beverage[menu] = beverage_ingredients
#     new_beverage[menu] = beverage_cost
#     menu.append(new_beverage)

# beverage("americano", "350 ml water", "3.5")

print(menu['espresso'].items())
