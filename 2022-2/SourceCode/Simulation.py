from Environment import Environment
from Agent import Agent

n = 7
m = 7
e1 = Environment(n,m,[0,0],[n-1,m-1])

ag = Agent(e1)
path = ag.act()

print(path)

e1.see_path(path)