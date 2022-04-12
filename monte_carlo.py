import random

def multiplicative_LCG(m,a):
    multiplicative_LCG.current = (a*multiplicative_LCG.current)%m
    return multiplicative_LCG.current/m


#Monte-Carlo method	using functional random	
def montecarlo(f,a,b,N,m,A):
	h = (b-a)/N
	F=[]
	G =[]
 	#using loop and random values to get list of x
	for i in range(0,N):
		X_i = a+(b-a)*multiplicative_LCG(m,A)
		#why the indentation errors argh
		F.append(f(X_i))
		G.append((f(X_i))**2)
		F_N = h*sum(F)

	#defining the sum integral function and its standard value
	F_N = h*sum(F)
	dev = (sum(G)/N - (sum(F)/N)**2)**0.5*2
	return F_N