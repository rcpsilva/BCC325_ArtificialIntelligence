import numpy as np
import matplotlib.pyplot as plt

class ToiletEnvironment():

    def __init__(self):
        self.number = 100
        self.max = 1000
        self.min = 0
        self.price = 1
        self.clock = 0

    def initialPercepts(self):
        return {
            "number": self.number,
            "max": self.max,
            "min": self.min,
            "price": self.price
        }

    def signal(self, action):
        """
            For a given action, return a percept
        """
        averageConsumption = [30, 80, 100, 80, 10, 2, 1]
        day = self.clock % 7

        self.number += action["to-buy"]
        self.number = min(self.number, self.max)
        demand = (averageConsumption[day] +
                        np.random.randn() * averageConsumption[day] / 10)
        self.number -= demand
        if (self.number < self.min):
            self.number = self.min

        self.price = 1 + (0.0005 * self.clock + np.random.randn()/10)
        self.price = abs(self.price)
        self.clock += 1

        return {
            "number": self.number,
            "number": self.number,
            "max": self.max,
            "min": self.min,
            "price": self.price,
            "demand":demand,
        }

if __name__ == "__main__":
    
    env = ToiletEnvironment()

    prices = []
    stock = []
    demand = [] 

    for i in range(10000):
        percepts = env.signal({'to-buy':0})
        prices.append(percepts['price'])
        stock.append(percepts['number'])
        demand.append(percepts['demand'])
        

    plt.plot(prices)
    plt.show()

    plt.plot(stock)
    plt.show()

    plt.plot(demand)
    plt.show()