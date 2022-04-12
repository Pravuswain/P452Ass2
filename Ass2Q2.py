import math
import monte_carlo as mc
import random

#Q2 part i
mc.multiplicative_LCG.current = 2000
inside = 0

n = 10000
X=[mc.multiplicative_LCG(1021,65) for i in range(n)]
Y = [mc.multiplicative_LCG(1021,65) for i in range(n)]



for i in range(n):
    x = X[i]
    y = Y[i]

    if ((x**2)+(y**2))<=1:
        inside += 1
        
    else:
        inside += 0
    
pi=(4*inside)/n
print ("The value of pi for random no generator with a =65 and m = 1021 is:")
print(pi)

#Q2 part ii
mc.multiplicative_LCG.current = 17000
inside = 0

n = 10000
X=[mc.multiplicative_LCG(16381,572) for i in range(n)]
Y = [mc.multiplicative_LCG(16381,572) for i in range(n)]



for i in range(n):
    x = X[i]
    y = Y[i]
    if ((x**2)+(y**2))<=1:
        inside += 1
        
    else:
        inside += 0
    
pi=(4*inside)/n
print ("The value of pi for random no generator with a =572 and m = 16381 is:")
print(pi)


#Q2 part iii
f = lambda x : 4*(1-x**2)**(0.5) 

out= mc.montecarlo(f,0,1,10000,16381,572)
print(f'Solution of Integral:')
print(out)


'''
The value of pi for random no generator with a =65 and m = 1021 is:
3.1516
The value of pi for random no generator with a =572 and m = 16381 is:
3.1464
Solution of Integral:
3.1463615619166063

'''