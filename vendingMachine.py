class VendingMachine:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    profit = 0
    coffee_dict = {}

    def turnOn(self, is_on=True):

        while is_on:

            selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

            match selection:
                case "off":
                    print("Machine shutting down...")
                    is_on = False
                case "report":
                    self.printReport()
                case _:
                    if selection in self.coffee_dict:
                        if self.checkResources(self.coffee_dict[selection]):
                            if self.getCoins(self.coffee_dict[selection]):
                                self.makeCoffee(self.coffee_dict[selection])
                    else:
                        print("Please select a coffee from the list.")

    def makeCoffee(self, coffee):
        self.resources["water"] -= coffee.getWater()
        self.resources["milk"] -= coffee.getMilk()
        self.resources["coffee"] -= coffee.getCoffee()

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

        if total < coffee.getCost():
            print("Sorry that's not enough money. Money refunded.")
            return False
        else:
            change = total - coffee.getCost()
            if total > coffee.getCost():
                print(f"Here is ${round(change, 2)} in change.")

            self.profit += total - change
            return True

    def printReport(self):
        print(
            f"Water: {self.resources.get('water')}ml\n"
            f"Milk: {self.resources.get('milk')}ml\n"
            f"Coffee: {self.resources.get('coffee')}g\n"
            f"Money: ${self.profit}"
        )