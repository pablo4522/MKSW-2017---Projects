import matplotlib.pyplot as plt
from SDToolbox import *
from matplotlib.legend_handler import HandlerLine2D

#INITIAL CONDITIONS
P1=one_atm; 
T1=300;
mech = 'wang_highT.cti';

n_h = 15
n_p = 5


CJ=np.zeros((n_h,n_p))  #CJ SPEED
P=np.zeros((n_h,n_p))     #PRESSURE
T=np.zeros((n_h,n_p))     #TEMPERATURE
CH=np.zeros((n_h,n_p))  #CONCENTRATION
CP=np.zeros((n_h,n_p))

for i in range(n_p):
    for k in range(n_h):
        c_h=.04*k+0.025
        c_p=.06*i
        ''' 
        A=np.zeros((2,2))
        A[0,0] = 1-c_h
        A[0,1] = -c_h
        A[1,0] = -c_p
        A[1,1] = 1-c_p
        
        b=np.zeros(2)
        b[0] = c_h
        b[1] = c_p
        x = np.linalg.solve(A,b) #SOLVING THE MOLE NUMBERS'''
        
        q='C3H8:{0} CH4:{1} O2:{2}'.format(c_p, c_h, 1-c_p-c_h) #SETTING COMPOSITION
    
        [cj_speed,R2] = CJspeed(P1, T1, q, mech, 0);    #CALCULATING CJ SPEED
        gas = PostShock_eq(cj_speed, P1, T1, q, mech)   #CALCULATING POST-SHOCK STATE 
        P[k,i] = gas.P/one_atm
        T[k,i] = gas.T
        CJ[k,i] = cj_speed  
        CH[k,i] = c_h
        CP[k,i] = c_p
        print k, i

plt.figure(1)
line1, =plt.plot(CH[:,0],P[:,0], "r-", label="0% C3H8")
line2, =plt.plot(CH[:,1],P[:,1], "g-", label="5% C3H8")
line3, =plt.plot(CH[:,2],P[:,2], "b-", label='10% C3H8')
line4, =plt.plot(CH[:,3],P[:,3], "y-", label='15% C3H8')
line5, =plt.plot(CH[:,4],P[:,4], "k-", label='20% C3H8')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=5, mode="expand", borderaxespad=0.)
plt.xlabel('H2 Concentration')
plt.ylabel('Pressure [bar]')
plt.figure(2)
line1, =plt.plot(CH[:,0],T[:,0], "r-", label="0% C3H8")
line2, =plt.plot(CH[:,1],T[:,1], "g-", label="5% C3H8")
line3, =plt.plot(CH[:,2],T[:,2], "b-", label='10% C3H8')
line4, =plt.plot(CH[:,3],T[:,3], "y-", label='15% C3H8')
line5, =plt.plot(CH[:,4],T[:,4], "k-", label='20% C3H8')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=5, mode="expand", borderaxespad=0.)
plt.xlabel('H2 Concentration [%]')
plt.ylabel('Temperature [K]')
plt.figure(3)
line1, =plt.plot(CH[:,0],CJ[:,0], "r-", label="0% C3H8")
line2, =plt.plot(CH[:,1],CJ[:,1], "g-", label="5% C3H8")
line3, =plt.plot(CH[:,2],CJ[:,2], "b-", label='10% C3H8')
line4, =plt.plot(CH[:,3],CJ[:,3], "y-", label='15% C3H8')
line5, =plt.plot(CH[:,4],CJ[:,4], "k-", label='20% C3H8')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=5, mode="expand", borderaxespad=0.)
plt.xlabel('H2 Concentration')
plt.ylabel('CJ speed [m/s]')
'''
plt.subplot(3,1,1)
plt.plot(Conc,P)
plt.xlabel('Concentration [%]')
plt.ylabel('Pressure [bar]')
plt.subplot(3,1,2)
plt.plot(Conc,T)
plt.xlabel('Concentration [%]')
plt.ylabel('Temperature [K]')
plt.subplot(3,1,3)
plt.plot(Conc,CJ)
plt.xlabel('Concentration [%]')
plt.ylabel('CJ speed [m/s]')

f = open('output.txt', 'w')
for j in range(40):
    f.write('%f \t %f \t %f \t %f \n' %(Conc[j], P[j], T[j], CJ[j]))
    
f.close
'''
np.savetxt("p.txt", P, delimiter = ',')
np.savetxt("t.txt", T, delimiter = ',')
np.savetxt("cj.txt", CJ, delimiter = ',')

print P