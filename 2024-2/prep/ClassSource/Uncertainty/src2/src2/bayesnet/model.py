import torch
from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork

device = torch.device("cpu")  # Or "cuda" if you want to use GPU


rain_dist = Categorical(torch.tensor([[0.7, 0.2, 0.1]], device=device))
rain_dist.labels = ["none", "light", "heavy"]
rain_dist.name = "rain"

maintenance_dist = ConditionalCategorical(
    torch.tensor([
        [0.4, 0.6],
        [0.2, 0.8],
        [0.1, 0.9],
    ], device=device)
)
maintenance_dist.labels = ["yes", "no"]
maintenance_dist.name = "maintenance"

# Follow similar patterns for other distributions


# Conditional probability table for train
train_dist = ConditionalCategorical(
    torch.tensor([
        [0.8, 0.2],  # "none", "yes"
        [0.9, 0.1],  # "none", "no"
        [0.6, 0.4],  # "light", "yes"
        [0.7, 0.3],  # "light", "no"
        [0.4, 0.6],  # "heavy", "yes"
        [0.5, 0.5],  # "heavy", "no"
    ], device=device)
)
train_dist.labels = ["on time", "delayed"]
train_dist.name = "train"

# Conditional probability table for appointment
appointment_dist = ConditionalCategorical(
    torch.tensor([
        [0.9, 0.1],  # "on time"
        [0.6, 0.4],  # "delayed"
    ], device=device)
)
appointment_dist.labels = ["attend", "miss"]
appointment_dist.name = "appointment"

# Create a Bayesian Network and add distributions
model = BayesianNetwork()
model.add_states(rain_dist, maintenance_dist, train_dist, appointment_dist)

# Add edges connecting nodes (define parent-child relationships here)
model.add_edge(rain_dist, maintenance_dist)
model.add_edge(rain_dist, train_dist)
model.add_edge(maintenance_dist, train_dist)
model.add_edge(train_dist, appointment_dist)

# Finalize the model
model.bake()

print("Bayesian Network created successfully!")
