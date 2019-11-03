from helpers import *
from random import choices

# load data
data = loadData()
mu = len(data)

# initial population N = 101
population = initPopulation(mu)
previousError = 1e10

for generation in range(150):
	parents = choices(population, k=mu*5) # parents population N = 505
	offsprings = mutate(parents) 
	population = fitness(offsprings, data)

	error = min([pop['error'] for pop in population])
	print(f"{generation:3}: {error:.3f}")
	
	if abs(error - previousError) < 1e-3:
		break
	previousError = error

print(population[0])
plotResults(data, population[0])