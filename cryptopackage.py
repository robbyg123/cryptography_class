
def GCD_linear_combined(a,b):
	u = 1
	g = a 
	x = 0 
	y = b 
	while y < 0 or y >0:
		t = int(g % y)
		q = int(g // y)
		s = int(u - q*x)
		u = x 
		g = y
		x = s 
		y = t 
	v = int((g-a*u)/b)
	while u < 0:
		u = int(u + b/g) 
		v = int(v - a/g)  
	return g, u, v


def GCD(a,b):
	u = 1
	g = a 
	x = 0 
	y = b 
	while y < 0 or y >0:
		t = int(g % y)
		q = int(g // y)
		s = int(u - q*x)
		u = x 
		g = y
		x = s 
		y = t 
	v = int((g-a*u)/b)
	while u < 0:
		u = int(u + b/g) 
		v = int(v - a/g)  
	return g


def modularinversecalc(a, N ):
	 g, inverse , v = GCD_linear_combined(N, a)
	 return inverse

def modularinversecalcV2(a, N ):
	 g, inverse , v = GCD_linear_combined(N, a)
	 if g != 1:
	 	return FALSE , g
	 return TRUE , inverse	

def quickpower( N, g, A):
	a = g
	b = 1
	while A>0:
		if 1 == (A % 2):
			b = b * a 
			b = b % N
		a = (a**2) % N
		A = A//2
	return b 

def polard_rho(N):
	a = 2 
	for j in range (2, int(N**.5)):
		a = (a*2) % N
		d = GCD(a-1, N)
		if 1 < d < N:
			return d, N/d 
	return 1 

def converttobase26(x):
	stringofvalues = []
	basecounter = 26
	counter = 0
	while basecounter < x:
		basecounter = basecounter*26
		counter = counter + 1
	second_temp_value = x 
	for i in range(0, counter +1,):
		i = counter-i
		temp_value = second_temp_value // (26**i)
		second_temp_value = second_temp_value % (26**i)

		stringofvalues.append(temp_value)
	return stringofvalues

"""
#10b
lm = 184437306609138

ln= 298332504337824
print(GCD_linear_combined(ln,lm))
#10c 
pair1 = int((70583995*4911157)-1)
pair2 = int((173111957*7346999)-1)
pair3 = int((180311381*29597249)-1)
print(pair1, pair2, pair3)
print(GCD_linear_combined(pair1, pair2))
firstgcd = 37498566
print(GCD_linear_combined(firstgcd, pair3))
"""