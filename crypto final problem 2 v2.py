import cryptopackage as cp 
import Ecurvepackage as ep 
import random 


# this is listras algorythmn as stated in the book with the random variable generation, use with caution for big numbers
def linstrafactorization( N):
	A = random.randrange(1,N)
	print("A = " , A)
	p1 = random.randrange(1,N)
	print("p1 = " , p1)
	p2 = random.randrange(1,N)
	print("p2 = " , p2)
	B = int(((p2**2) - (p1**3) - (A*p1)) % N)
	print ("B =" , B)
	for j in range(1, 200):
		Q1 , Q2 = ep.doubleAndAddECV2(p1, p2, j , A, B, N)
		if Q1 == "fail":
			if Q2 != N:
				return Q2
			if Q2 == N:
				return linstrafactorization( N)
		p1 = Q1
		p2 = Q2

# this is a test case from the book that consistently works with randomly generated constants 
print(linstrafactorization( 6887))

B = -453
A = 18
p1 = 7
p2 = 4 
N = 28102844557
def linstrafactorizationFortest( N, A,  B, p1, p2):
	for j in range(1, 10000):
		Q1 , Q2 = ep.doubleAndAddECV2(p1, p2, j , A, B, N)
		if Q1 == "fail":
			if Q2 != N:
				return Q2
			if Q2 == N:
				return linstrafactorization( N)
		p1 = Q1
		p2 = Q2


print(linstrafactorizationFortest(N, A,  B, p1, p2))

# this returns 238639 which is one of the factors of N! 


#the functions used in the function are modified versions of ones used earlier in class. They are in my two packages as they are called here but 
#the packages are rather poorly organized so i will paste them in below as a comment for convinence. 
#the modifications where made for the eliptic curve adder to be able to detect when the inverse calculation will fail and then be able to communicate that
#while being called by the double and add algorythmn 

"""
def modularellipticcurveadderV2( P1, P2, Q1 , Q2, A , B , M ):
	if P1 == "O"  and P2 == "O":
		return Q1 , Q2 
	if Q1 == "O" and Q2 == "O":
		return P1 , P2
	if P1 == Q1 and Q2 == -P2:
		return "O" , "O"
	if P1 == Q1 and Q2 == P2:
		dummy = (2*P2)
		if cp.GCD(M,dummy) != 1 and cp.GCD(M,dummy) -1 :
			return "fail", cp.GCD(M,(2*P2))
		lamda = (3.*(P1**2) + A)*cp.modularinversecalc(M,(2* P2)) % M
	if P1 != Q1 or Q2 != P2:
		dummy = Q1 - P1
		if cp.GCD(M,dummy) != 1 and cp.GCD(M,dummy) != -1 :
			return "fail", cp.GCD(M,(Q1-P1))
		lamda = 1.*(Q2 - P2)*cp.modularinversecalc(M,(Q1-P1)) % M
	x = ((lamda**2) - P1 - Q1) % M
	y = (lamda*(P1-x)-P2) % M
	return x, y
"""



"""
def doubleAndAddECV2(P1,P2, N,  A,B, M):
	Q1 = P1
	Q2 = P2
	R1 = "O"
	R2 = "O"
	while N > 0:
		if (N % 2) == 1:
			R1 , R2 = modularellipticcurveadderV2(R1, R2, Q1, Q2, A, B, M)
			if R1 == "fail":
				return R1, R2
		Q1 , Q2 = modularellipticcurveadderV2(Q1, Q2, Q1, Q2, A, B, M)
		if Q1 == "fail":
			return Q1, Q2
		N = N//2  
	return R1, R2 
"""