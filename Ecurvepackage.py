import cryptopackage as cp

# this program takes in constants A ,B and modulo M and finds all values that satisfy the equation y^2 = x^3 + Ax + B mod M 
# it was used on problems 6.5, 6.7
def ellipticcurvesoltioncalc(A,B,M):
	listofsolutions = [] 
	for i in range (0,M): 
		for j in range (0, M):
			if (i**3 + A*i + B )% M == (j**2) % M:
				listofsolutions.append((i, j))
	return(listofsolutions)



# this adds two points on an elliptic curve that are not inverses or the idenity, Not modular 
def ellipticcurveadder( P1, P2, Q1 , Q2, A , B ):
	if P1 == Q1 and Q2 == P2:
		lamda = (3.*(P1**2) + A)/(2* P2)
	if P1 != Q1 or Q2 != P2:
		lamda = 1.*(Q2 - P2)/(Q1-P1)
	x = (lamda**2) - P1 - Q1 
	y = lamda*(P1-x)-P2 
	return x, y

#this checks if a point is on the elliptic curve 
def ellpiticcurvechecker(x, y, A, B):
	if (x**3 + A*x + B ) - y**2 < .00005:
		print "sucess"
	else:
		print "fail"



# 6.1 a 
a,b = ellipticcurveadder(3,-5,3,-5,-2,4)



# a, b = (0.25, -1.875)

#6.1 b
c,d = ellipticcurveadder(0,2,0,2,-2,4)



# c,d = (0.25, -1.875)

#6.1 c part 1 e,f = (240.0, 3718.0)
e,f = ellipticcurveadder(c,d,0,2,-2,4)


#6.1 c part 2 g, h (-1.958677685950413, -0.6348610067618328)
g,h = ellipticcurveadder(c,d,3,-5,-2,4)



#this adds two points on the ellipic curve in mod M
def modularellipticcurveadder( P1, P2, Q1 , Q2, A , B , M ):
	if P1 == "O"  and P2 == "O":
		return Q1 , Q2 
	if Q1 == "O" and Q2 == "O":
		return P1 , P2
	if P1 == Q1 and Q2 == -P2:
		return "O" , "O"
	if P1 == Q1 and Q2 == P2:
		lamda = (3.*(P1**2) + A)*cp.modularinversecalc(M,(2* P2)) % M
	if P1 != Q1 or Q2 != P2:
		lamda = 1.*(Q2 - P2)*cp.modularinversecalc(M,(Q1-P1)) % M
	x = ((lamda**2) - P1 - Q1) % M
	y = (lamda*(P1-x)-P2) % M
	return x, y

# this has an additional check to make sure the inverse that must be calculated exists, made for use in linsta's algorythmn. 
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


# this verifies points are on the curve mode M
def modularellpiticcurvechecker(x, y, A, B, M):
	if ((x**3 + A*x + B ) - y**2 ) % M == 0:
		print "sucess"
	else:
		print "fail"

# 6.8 
q, w = modularellipticcurveadder( 4,2, 4,2,  1 , 1 , 5 )

# q, w =3,4

q2, w2 = modularellipticcurveadder( q,w, 4,2,  1 , 1 , 5 )

#q2,w2 = 2, 4

q3, w3 = modularellipticcurveadder( q2,w2, 4,2,  1 , 1 , 5 )

#q3, w3 = 0 , 4 

q4, w4 = modularellipticcurveadder( q3,w3, 4,2,  1 , 1 , 5 )

#q4, w4 = 0,1

# so n = 5 for n(4,2) = (0,1) mod 5 




# 11 d) 
def doubleAndAddEC(P1,P2, N,  A,B, M):
	Q1 = P1
	Q2 = P2
	R1 = "O"
	R2 = "O"
	while N > 0:
		if (N % 2) == 1:
			R1 , R2 = modularellipticcurveadder(R1, R2, Q1, Q2, A, B, M)
		Q1 , Q2 = modularellipticcurveadder(Q1, Q2, Q1, Q2, A, B, M)
		N = N//2  
	return R1, R2 
#this is a check of the example from the book and it was right!
doubleAndAddEC(6,730, 947 , 14, 19 , 3623)

# this is the problem from the homework
doubleAndAddEC(2898, 439, 3211 , 1541, 1335 , 3221)


# the output was 243, 1875


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
print(doubleAndAddECV2(2898, 439, 3211 , 1541, 1335 , 3221))
# this test works





# this does the binary expansion for 6.12 d)
def binaryexpansion(n):
	x = []
	while n > 0:
		if (n % 2) == 1:
			x.append(1)
		elif (n % 2) == 0:
			x.append(0)
		n = n//2
	x.reverse()
	return x 



# this code does the ternary expansion from the book for 12 d)
def ternaryexpansion(n):
	x = binaryexpansion(n)
	x.reverse()
	g = 0
	while g< len(x):
		if x[g] == 1 and x[g+1] == 1:
			x[g] = -1
			g += 1
			if g >= len(x):
				x.append(1)
				return x  
			while x[g] == 1:
				x[g] = 0
				g += 1
				if g >= len(x):
					x.append(1)
					return x
			x[g] = 1
		else:
			g = g + 1
		



	return x


# this is a check for the turinary expansion and it work!

x = ternaryexpansion(8379483273489)

t=0
for i in range(0,len(x) ):
	if x[i] == 1:
		t = (2**i) + t
	if x[i] == -1:
		t = t - (2**i)


# the output for ternaryexpansion(8379483273489) is [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, -1, 0, 0, 0, 1]

#6.14 a)
doubleAndAddEC(1980 ,431, 1943,  171, 853, 2671)

#this output (1432.0, 667.0)

#6.14 b)

doubleAndAddEC(2110 , 543, 1943,  171, 853, 2671)

#(2424.0, 911.0)

#6.14 C ) that would require a way to solve the discrete log problem
R1 = 2110
R2 = 543
P1 = 1980
P2 = 431
M = 2671
A = 171
B = 853

x = modularellipticcurveadder( P1, P2, P1 , P2, A , B , M )
n = 0
while x[0] != 2110 or x[1] != 543:
	x = modularellipticcurveadder(P1, P2, x[0], x[1] , A, B, M )
	n += 1 


# n = 724


#14 d) 
y_squared = 2**3 + 171*2 + 853

y = (y_squared**(2672/4)) % 2671


doubleAndAddEC(2, y, 875, 171, 853, 2671)

# this returns (1708.0, 1419.0) so x is 1708


# 6.16 b)


y_squared = 278**3 + 54*278 + 87 


y = (y_squared**(1124/4)) % 1123



# this gives y = 487 if the bit is 0 then its 487
# if the bit is 1 then it gives -487 mod 1123


#6.17c 

M = 1201
A = 19
B = 17 
P1 = 278
P2 = 285
N = 595 
R1 = 1147 
R2 = 640

doubleAndAddEC(P1,P2, N,  A,B, M)
# this prints (1104.0, 492.0)

doubleAndAddEC(R1,R2, N,  A,B, M)
#this prints (942.0, 476.0)

xtinv = cp.modularinversecalc(M,942)
ytinv = cp.modularinversecalc(M,476)

m1 = (xtinv*279) % M
m2 = (ytinv*1189) % M

#this prints 509 767


#6.18 b)

c1 = 814
c2 = 1050
m1 = 1050
p = 1201
m1inv = cp.modularinversecalc(p,m1)
A = 19
B = 17











