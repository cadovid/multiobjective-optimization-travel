from platypus import *

def coste(vars):
    dist_tren = vars[0]
    a = 0.2
    b = 0.9
    c = 30
    d = 50
    e = 11.41
    return [dist_tren**(1/a) + (e - dist_tren)**(1/b), dist_tren/c + (e - dist_tren)/d]

problem = Problem(1, 2)
problem.types[:] = Real(0, 11.41)
problem.function = coste

algorithms = [NSGAII, (NSGAIII, {"divisions_outer":12}), GDE3, IBEA, SMPSO, SPEA2]
results = experiment(algorithms, problem, seeds=1, nfe=10000)

# display the results
import matplotlib.pyplot as plt
point_type = ['r.','bx','g^','cs','m+','k1']

# one subplot per algorithm
fig = plt.figure()

for i, algorithm in enumerate(six.iterkeys(results)):
    result = results[algorithm]["Problem"][0]
    
    ax = fig.add_subplot(2, 3, i+1)
    ax.set_axisbelow(True)
    ax.grid()
    ax.scatter([s.objectives[0] for s in result],
               [s.objectives[1] for s in result])
    ax.set_xlabel('C(x,y)')
    ax.set_ylabel('T(x,y)')
    ax.set_title(algorithm)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()

# all results together
fig = plt.figure()
plt.grid()

for i, algorithm in enumerate(six.iterkeys(results)):
    result = results[algorithm]["Problem"][0]
    
    plt.plot([s.objectives[0] for s in result],
             [s.objectives[1] for s in result], point_type[i], label=algorithm)

plt.xlabel('C(x,y)')
plt.ylabel('T(x,y)')
plt.title('Todos los algoritmos')
plt.legend(loc='upper right')

plt.show()