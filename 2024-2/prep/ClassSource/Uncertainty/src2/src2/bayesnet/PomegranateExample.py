import seaborn; seaborn.set_style('whitegrid')
import torch
import numpy

from pomegranate.distributions import Categorical
from pomegranate.distributions import ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork

d1 = Categorical([[0.1, 0.9]])
d2 = ConditionalCategorical([[[0.4, 0.6], [0.3, 0.7]]])

model = BayesianNetwork([d1, d2], [(d1, d2)])

model2 = BayesianNetwork()
model2.add_distributions([d1, d2])
model2.add_edge(d1, d2)

X = numpy.random.randint(2, size=(10, 2))

model.fit(X)

print(model.distributions[0].probs) 
print(X[:,0].mean())