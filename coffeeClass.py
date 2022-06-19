class Coffee:

    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.water = water
        self.coffee = coffee
        self.milk = milk
        self.cost = cost

    def getResource(self, string):

        if string == "water":
            return self.water
        elif string == "coffee":
            return self.coffee
        elif string == "milk":
            return self.milk
        elif string == "cost":
            return self.cost