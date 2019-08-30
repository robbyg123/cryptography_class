import math
import cryptopackage as cp 

def babystepgiantstep ( N, g, h):
	n = int(1 + math.sqrt(N))
	list1 = []
	list2 = []
	dummy = (g**n)% N
	u = int(cp.modularinversecalc(dummy, N))
	for i in range(0, n+1):
		b = (g**i) % N
		list1.append(b)
		a =(h*(u**i)) % N 
		list2.append(a)
	for i in range(0, n):
		for j in range(0, n):
			if list1[i] == list2[j]:
				return (i + (j*n))
print(babystepgiantstep(71, 11, 21))
print(babystepgiantstep(593, 156, 116))
print(babystepgiantstep(3571, 650, 2213))

