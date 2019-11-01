from helpers import *
from random import choices

# load data
data = loadData()
mu = len(data)

# initial population N = 101
population = initPopulation(mu)
print(population[0])

# parents population N = 505
parents = choices(population, k=mu*5)
print(parents[0])

offsprings = mutate(parents)
print(offsprings[0])
