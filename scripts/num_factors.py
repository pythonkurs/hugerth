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

def dict_add (dic, element):
	if element in dic:
		dic[element] += 1
	else:
		dic[element] = 1

lengths = dict()

#For every number from 2 to 500K:

	factors = factorize()#number

	dic = dict()

	for element in factors:
		dict_add(dic, element)

	dict_add (lengths, len(dic))



print lengths

