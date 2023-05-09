from Environment import Environment
from Agent import Agent, GreedyAgent

n = 10
m = 10
e1 = Environment(n,m,[1,1],[n-1,m-1])

ag = GreedyAgent(e1)
path = ag.act()

print(path)

e1.see_path(path)