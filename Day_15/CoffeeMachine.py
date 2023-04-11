from Resourse import resources
from Resourse import MENU
from os import system

# TODO 1. Ask question "What would you like? (espresso/latte/cappuccino)"
# TODO 2. Make a while in a true or false variable
# TODO 3. Check the resource before insert enough money
# TODO 4. Want a money (quarters/dimes/nickles/pennies) = ($0.25, $0.10, $0.5, $0.01)
# TODO 5. Calculate given the money (each number multiply calculate with amount)
# TODO 6. Check that you have received enough money from user
# TODO 7. if the money is enough then we can give a user's coffee but if not then print error message
# TODO 8. There are three if condition 1C. 'report', 2C. which Coffee, 3C. OFF


def display_repo(money):
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(money))


def check_resource(condition):
    take = MENU[condition]
    water = take["ingredients"]["water"]
    coffee = take["ingredients"]["coffee"]
    milk = 0
    if condition != "espresso":
        milk = take["ingredients"]["milk"]

    if water > resources["water"]:
        print("Sorry! There is not enough water")
        return False
    elif milk != 0 and milk > resources["milk"]:
        print("Sorry! There is not enough milk")
        return False
    elif coffee > resources["coffee"]:
        print("Sorry! There is not enough coffee")
        return False
    else:
        resources["water"] -= water
        resources["coffee"] -= coffee
        if milk != 0:
            resources["milk"] -= milk
    return True


def if_coffee(condition):
    if condition == "espresso" and check_resource(condition):
        return True
    elif condition == "latte" and check_resource(condition):
        return True
    elif condition == "cappuccino" and check_resource(condition):
        return True
    return False


def make_coffee(condition):
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    total -= MENU[condition]["cost"]
    if total < 0:
        print("This money is not enough! if you want to coffee then you have to give more money")
        return 0
    print(f"Here is ${total} in change.")
    print(f"Here is your {condition} ☕ Enjoy!")
    return MENU[condition]["cost"]


is_true = True
money = 0

while is_true:
    condition = input("What would you like? (espresso/latte/cappuccino): ")
    if condition == "off":
        is_true = False
    elif condition == "report":
        display_repo(money)
    elif if_coffee(condition):
        money += make_coffee(condition)

system("rm -rf __pycache__")