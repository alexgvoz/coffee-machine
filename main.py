import coffeeClass
import vendingMachine

if __name__ == '__main__':
    machine = vendingMachine.VendingMachine()

    machine.coffee_list.append(coffeeClass.Coffee("latte", 200, 24, 150, 2.5))
    machine.coffee_list.append(coffeeClass.Coffee("espresso", 50, 18, 0, 1.5))
    machine.coffee_list.append(coffeeClass.Coffee("cappuccino", 250, 24, 100, 3.0))

    machine.turnOn()