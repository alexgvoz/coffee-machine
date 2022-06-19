class VendingMachine:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    profit = 0
    coffee_list = []

    def turnOn(self, is_on=True):

        while is_on:
            selection = input("What would you like? (espresso/latte/cappuccino): ")

            if selection == "off":
                print("Machine shutting down...")
                is_on = False
            elif selection == "report":
                print(
                    f"Water: {self.resources.get('water')}ml\n"
                    f"Milk: {self.resources.get('milk')}ml\n"
                    f"Coffee: {self.resources.get('coffee')}g\n"
                    f"Money: ${self.profit}"
                )
            else:
                for c in self.coffee_list:
                    if c.name.lower() == selection.lower():
                        if self.checkResources(c):
                            if self.getCoins(c):
                                self.makeCoffee(c)

    def makeCoffee(self, coffee):
        for item in self.resources:
            self.resources[item] -= coffee.getResource(item)

        print(f"Enjoy your {coffee.name}!")

    def checkResources(self, res):
        for item in self.resources:
            if self.resources[item] - res.getResource(item) > 0:
                pass
            else:
                print(f"Sorry there is not enough {item}.")
                return False

        return True

    def getCoins(self, coffee):
        print("Please insert coins.")
        total = float(input("How many quarters?: ")) * 0.25
        total += float(input("How many dimes?: ")) * 0.1
        total += float(input("How many nickles?: ")) * 0.05
        total += float(input("How many pennies?: ")) * 0.01

        if total < coffee.getResource("cost"):
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = total - coffee.getResource('cost')
            if total > coffee.getResource("cost"):
                print(f"Here is ${round(change, 2)} in change.")

            self.profit += total - change
            return True