from agents import *
from environment import *

G = {'A':['B','G','C'],
     'B':['D','E'],
     'C':['F'],
     'D':['G'],
     'E':[],
     'F':['G','H'],
     'G':[],
     'H':[]}


env = Environment(G=G,start='A',goal='G')
ag = BFS(env)
goal = ag.search()
print(f'BFS: /n {ag.get_path(goal)}')

ag = DFS(env)
goal = ag.search()
print(f'DFS: /n {ag.get_path(goal)}')