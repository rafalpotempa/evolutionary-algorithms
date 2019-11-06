from helpers import *
from random import choices
from time import time

# load data
data = loadData()
mu = 101

# initial population N = 101
population = initPopulation(mu)
previousError = 1e10

start = time()
for generation in range(150):
	parents = choices(population, k=mu*5) # parents population N = 505
	offsprings = mutate(parents) 
	population = fitness(offsprings, data)

	error = min([pop['error'] for pop in population])
	print(f"{generation:3}: {error:.3f}")
	
	if abs(error - previousError) < 1e-5:
		break
	previousError = error
end = time()

print(population[0])
plotResults(data, population[0])
print(f"Time elapsed: {end - start} s")