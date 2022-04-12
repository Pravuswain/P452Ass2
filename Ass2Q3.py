import monte_carlo as mc

f2 = lambda x : 4*(1-x**2)

#setting a seed
mc.multiplicative_LCG.current = 2000

out2 = mc.montecarlo(f2,-1,1,1000,16381,572)
print(f'Volume of steinmetz solid using the Multiplicative LCG of m = 16381 and a =572')
print(out2)

'''
Volume of steinmetz solid using the Multiplicative LCG of m = 16381 and a =572
5.279081603281913
'''