from helpers import *

# load data
data = loadData()

mu = len(data)
# initial population N = 101
population = initPopulation(mu)
print(population)

exit()

# parents population N = 505
parents = choices(population, k=mu*5)
print(parents[0])

offsprings = mutate(parents)
print(offsprings[0])