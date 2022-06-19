class Coffee:

    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.cost = cost

    def getResource(self, resource):

        match resource:
            case "water":
                return self.getWater()
            case "coffee":
                return self.getCoffee()
            case "milk":
                return self.getMilk()

    def getWater(self):
        return self.water

    def getCoffee(self):
        return self.coffee

    def getMilk(self):
        return self.milk

    def getCost(self):
        return self.cost