from Machine_Menu import MENU


def check(w, m, c, w1, m1, c1):
    if w1 - w >= 0:
        if m1 - m >= 0:
            if c1 - c >= 0:
                return "All good"
            else:
                return "Coffee"
        else:
            return "Milk"
    else:
        return "Water"


def coffee_machine():
    on = True
    water = 300
    milk = 200
    coffee = 100
    money = 0.00
    while on:
        choice = input("What would you like? (espresso/latte/cappuccino)  ").lower()
        if choice != "report" and choice != "off":
            choice_water = MENU[choice]["ingredients"]["water"]
            choice_milk = MENU[choice]["ingredients"]["milk"]
            choice_coffee = MENU[choice]["ingredients"]["coffee"]
        moneyf = '{0:.2f}'.format(money)
        if choice == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${moneyf}")
        elif choice == "off":
            on = False
        else:
            if check(w=choice_water, m=choice_milk, c=choice_coffee, w1=water, m1=milk, c1=coffee) == "Water":
                print("Sorry, there is not enough water.")
            elif check(w=choice_water, m=choice_milk, c=choice_coffee, w1=water, m1=milk, c1=coffee) == "Milk":
                print("Sorry, there is not enough milk.")
            elif check(w=choice_water, m=choice_milk, c=choice_coffee, w1=water, m1=milk, c1=coffee) == "Coffee":
                print("Sorry, there is not enough coffee")
            else:
                print(f"The price of a {choice} is ${MENU[choice]['cost']}0")
                print("Please insert coins.")
                q = int(input("How many quarters?:  "))
                d = int(input("How many dimes?:  "))
                n = int(input("How many nickels?:  "))
                p = int(input("How many pennies?:  "))
                money_inserted = (q*25 + d*10 + n*5 + p*1)/100
                diff = round(money_inserted - MENU[choice]["cost"], 2)
                money += MENU[choice]["cost"]
                if diff >= 0:
                    if diff >0:
                        print(f"Here is ${diff} in change.")
                    print(f"Enjoy your {choice.title()}!")
                    water -= MENU[choice]["ingredients"]["water"]
                    milk -= MENU[choice]["ingredients"]["milk"]
                    coffee -= MENU[choice]["ingredients"]["coffee"]
                else:
                    money -= MENU[choice]["cost"]
                    print("Sorry, that\'s not enough money. Money refunded.")


coffee_machine()
