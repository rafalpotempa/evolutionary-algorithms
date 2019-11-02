from random import seed, uniform, gauss
from math import exp, cos, pi
import matplotlib.pyplot as plt

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
		'error': 0,
    	'x': 	 [uniform(-10, 10) for i in range(3)],
  		'sigma': [uniform(1e-10, 10 - 1e-10) for i in range(3)]}
		for j in range(mu)]
	return population

def mutate(parents):
	offsprings = []
	for parent in parents:
		offsprings.append({
			'error': 0,
			'x': 	 [x + gauss(0, parent['sigma'][i]) for i, x in enumerate(parent['x'])],
			'sigma': [sigma * exp(tau1 * gauss(0, 1) * exp(tau2 * gauss(0, 1))) for sigma in parent['sigma']]
		})
	return offsprings

def meanSquareError(Y0, Y):
	return sum([(Y0[i] - y)**2 for i, y in enumerate(Y)]) / len(Y0)

def f(x, pop):
	a, b, c = pop['x']
	return a*(x**2 + b*cos(c*pi*x))

def fitness(population, data):
	mu = len(data)
	X, Y0, sorter = [], [], []
	[[X.append(point[0]), Y0.append(point[1])] for point in data]

	for i, pop in enumerate(population):
		Y = []
		for x in X:
			Y.append(f(x, pop))
		pop['error'] = meanSquareError(Y0, Y)
		sorter.append([pop['error'], i])
	
	sorter.sort()

	return [population[sorter[i][1]] for i in range(mu)]

def plotResults(data, pop):
	X, Y0, Y = [], [], []
	[[X.append(point[0]), Y0.append(point[1])] for point in data]
	for x in X:
		Y.append(f(x, pop))

	plt.plot(X, Y0, 'ro', X,  Y)
	plt.show()

if __name__ == "__main__":
	print("Run algorithm.py")
