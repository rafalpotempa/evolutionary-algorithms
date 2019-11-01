from random import seed, uniform, gauss
from math import exp

seed(0)
tau1 = 1/12**0.5
tau2 = 1/(2*6**0.5)**0.5

def loadData():
	data = []
	with open("data/AIdata10.dat") as file:
		[data.append([float(x) for x in line.split()]) for line in file]
	return data

def initPopulation(mu):
	population = [{
    	'x': 	 [uniform(-10, 10) for i in range(3)],
  		'sigma': [uniform(1e-10, 10 - 1e-10) for i in range(3)]}
		for j in range(mu)]
	return population

def mutate(parents):
	offsprings = []
	for parent in parents:
		offsprings.append({
			'x': 	 [x + gauss(0, parent['sigma'][i]) for i, x in enumerate(parent['x'])],
			'sigma': [sigma * exp(tau1 * gauss(0, 1) * exp(tau2 * gauss(0, 1))) for sigma in parent['sigma']]
		})
	return offsprings

def meanSquareError(Y0, Y):
	return sum([(Y0[i] - y)**2 for i, y in enumerate(Y)]) / len(Y0)

def fitness(population):
	pass