#polard rho factorization
import cryptopackage as cp
def polard_rho(N):
	a = 2 
	for j in range (2, int(N**.5)):
		a = (a*2) % N
		d = cp.GCD(a-1, N)
		if 1 < d < N:
			return d, N/d 
	return 1 

#3.22 a 
print (polard_rho(1739))
# output of (47,37)



# 3.22 b 
print (polard_rho(220459))
# output of (449, 491)




# 3.22c
print (polard_rho(48356747))
#output of (6991, 6917)

print(polard_rho(536813567))