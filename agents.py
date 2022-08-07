from environments import ToiletEnvironment
import matplotlib.pyplot as plt


class ToiletAgent:
    def __init__(self, env) -> None:
        self.percepts = env.initialPercepts()
        self.env = env
        self.spent = 0
        self.expected_demand = 0
        self.expected_cost = self.percepts['price'] 
        self.clock = 0

        # Tarefa:
        # Criar uma maneira de prever quando o agente deve comprar mais papéis higiênicos
        # E também quanto deve comprar, baseado no histórico de preço do papel
        # E o histórico de demanda de papel

    def act(self):
        stock = self.percepts["number"]
        critical = max(0, self.expected_demand - stock)

        to_buy = critical

        if self.percepts['price'] < self.expected_cost/2:
            to_buy *= 4
        elif self.percepts['price'] < self.expected_cost:
            to_buy *= 2

        to_buy = min(to_buy, self.percepts['max']-self.percepts['number'])

        self.spent = to_buy*self.percepts['price']
        self.to_buy = to_buy

        stock_before = self.percepts['number']

        self.percepts = self.env.signal({'to-buy':to_buy})
        self.clock += 1

        stock_after = self.percepts['number']

        self.expected_cost = (self.expected_cost*(self.clock-1) + self.percepts['price'])/self.clock  
        demand = stock_before - stock_after + to_buy
        self.expected_demand = (self.expected_demand*(self.clock-1) + demand)/self.clock

if __name__ == "__main__":
    env = ToiletEnvironment()
    ag = ToiletAgent(env)

    stock = []
    spendings = []
    bought = []
    exp_c = []
    exp_d = []

    for i in range(400):
        ag.act()
        stock.append(env.number)
        spendings.append(ag.spent)
        bought.append(ag.to_buy)
        exp_c.append(ag.expected_cost)
        exp_d.append(ag.expected_demand)

    
    plt.plot(stock)
    plt.title('stock')
    plt.show()

    plt.plot(spendings)
    plt.title('spendings')
    plt.show()

    plt.plot(bought)
    plt.title('bought')
    plt.show()

    plt.plot(exp_c)
    plt.title('exp_c')
    plt.show()

    plt.plot(exp_d)
    plt.title('exp_d')
    plt.show()
