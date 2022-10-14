from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
order_processor = CoffeeMaker()
payment_processor = MoneyMachine()
machine_is_running = True

while machine_is_running:
    user_input = input(f"What would you like?: {menu.get_items()} ").lower()
    if user_input == "report":
        order_processor.report()
        payment_processor.report()
    elif user_input == "off":
        machine_is_running = False
        print("Goodbye!")
    elif menu.find_drink(user_input):
        drink = menu.find_drink(user_input)
        if order_processor.is_resource_sufficient(drink):
            if payment_processor.make_payment(drink.cost):
                order_processor.make_coffee(drink)
