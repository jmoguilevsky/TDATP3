from itertools import repeat
from math import ceil

def bag_polinomial(n, capacity, weights, values, ids):
	epsilon = 0.2
	maxValues = max(values)
	print(maxValues)
	b = ((epsilon/(2*n))) * maxValues 
	print(b)
	values = map(lambda x: int(ceil(x / b)), values)

	vStar = max(values)
	V = n * int(vStar)

	m = [[0 for i in repeat(None, V + 1)] for j in repeat(None, n + 1)]
	for i in xrange(1, n + 1):
		valuesSum = sum([values[j - 1] for j in xrange(1, i + 1)])
		for v in xrange(1, valuesSum + 1) :
			if v > sum([values[j - 1] for j in xrange(1, i)]):
				m[i][v] = weights[i - 1] + m[i-1][max(0,v - values[i - 1])]
			else:
				m[i][v] = min(m[i - 1][v], weights[i - 1] + m[i - 1][max(0, v - values[i - 1])])

	solutions = [[m[n][j], j * b] for j in xrange(V)]
	valid = filter(lambda x: x[0] <= capacity, solutions)
	print('solution', max(valid, key=lambda x: x[0]))
