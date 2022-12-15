from Environment import Environment
from Agent import Agent

n = 15
m = 15
e1 = Environment(n,m,[5,5],[n-1,m-1])

ag = Agent(e1)
path = ag.act()

print(path)

e1.see_path(path)