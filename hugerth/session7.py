def factorize(n):
	if n < 2:
		return []
	factors = []
	p = 2
	while True:
		if n == 1:
			return factors
		r = n % p
		if r == 0:
			factors.append(p)
			n = n / p
		elif p * p >= n:
			factors.append(n)
			return factors
		elif p > 2:
			p += 2
		else:
			p += 1

def parallel():
	results = dict()

	def dict_add (dic, element):
		if element in dic:
			dic[element] += 1
		else:
			dic[element] = 1

	for n in numbers:
		if n < 2:
			return []
		factors = []
		p = 2
		while True:
			if n == 1:
				break
			r = n % p
			if r == 0:
				factors.append(p)
				n = n / p
			elif p * p >= n:
				factors.append(n)
				break
			elif p > 2:
				p += 2
			else:
				p += 1

		unique = set()
		for factor in factors:
			unique.add(factor)
		dict_add(results, len(unique))

	return results

	

def dict_add (dic, element):
	if element in dic:
		dic[element] += 1
	else:
		dic[element] = 1

def dict_sum (dic, key, value):
	if key in dic:
		dic[key] += value
	else:
		dic[key] = value

def multitask(args):
	factors = factorize (args)
	dic = dict()
	for element in factors:
		dict_add(dic, element)
	return len(dic)
