from itertools import repeat

def bag_polinomial(n, capacity, weights, values, ids):
	vStar = max(values)
	index = values.index(vStar)
	print('vstar', vStar)
	print('weight', weights[index])
	print('capacity', capacity)
	print('sum values', sum(values))
	V = n * vStar
	m = [[0 for i in repeat(None, V + 1)] for j in repeat(None, n + 1)]
	for i in xrange(0, n + 1):
		m[i][0] = 0

	for i in xrange(1, n + 1):
		valuesSum = sum([values[j - 1] for j in xrange(1, i + 1)])
		for v in xrange(1, valuesSum):
			if v > sum([values[j - 1] for j in xrange(1, i)]):
				m[i][v] = weights[i - 1] + m[i - 1][v]
			else:
				m[i][v] = min(m[i - 1][v], weights[i - 1] + m[i - 1][max(0, v - values[i - 1])])
