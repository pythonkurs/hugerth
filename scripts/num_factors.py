import sys
import os
import multiprocessing
from IPython.parallel import Client

lengths = dict()

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

def parallel(n):
	results = []
	dic = dict()
	returns = []
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

		results.append(factors)

		## Still inside this 'for' loop,
		## Do all the dictionary things.
		## Do I have to redefine them here?

	

def dict_add (dic, element):
	if element in dic:
		dic[element] += 1
	else:
		dic[element] = 1

def task(args):
	factors = factorize (args)
	dic = dict()
	for element in factors:
		dict_add(dic, element)
	return len(dic)


if __name__ == '__main__':

	if len (sys.argv) == 2:
		n = 500000
		mode = sys.argv[1]
		print "Using standard value 500000\n"

	elif len (sys.argv) == 3:
		n = int(sys.argv[2])
		mode = sys.argv[1]
		
	else:
		print "Please use the format 'num_factors.py <mode> <number>',"
		print "where mode is one of s(erial) m(ultiprocessing) or i(Python)."
		print "Number is an integer larger than 2. If omitted, 500000 is used.\n"

	n+=1

	if mode == 's':
		for number in range(2,n):
			factors = factorize(number)
			dic = dict()
			for element in factors:
				dict_add(dic, element)
			dict_add (lengths, len(dic))
	
	elif mode == 'm':
		cpus = multiprocessing.cpu_count()
		if cpus > 4:
			cpus = 4
		pool = multiprocessing.Pool(processes=cpus)
		result = pool.map(task, range(2,n))
		for length in result:
			dict_add(lengths, length)

	elif mode == 'i':
		cli = Client()
		dview = cli[:]
		result = dview.scatter('numbers', range(2,n), block=False)
		print result
		for element in result:
			print element
		#list_of_dists = dview.apply_sync(parallel)

	else:
		print "Please select one of s(erial), m(ultiprocessing) or i(Python) modes\n"		

print lengths

