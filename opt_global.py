from platypus import *
import math

def travel(vars):
    x1 = vars[0]
    x2 = vars[1]
    x3 = vars[2]
    a1 = 57
    a2 = 54
    a3 = 49
    b1 = 3
    b2 = 1
    b3 = 5
    return [(a1*x1+b1)+(a2*math.log(x2 +1)+b2)+(a3*math.tanh(x3)+b3), 
            -(x1+x2+x3)], [x1+x2+x3-1, 
                           (a1*x1+b1)+(a2*math.log(x2 +1)+b2)+(a3*math.tanh(x3)+b3)-80]

problem = Problem(3, 2, 2)
problem.types[:] = [Real(0, 1), Real(0, 1), Real(0, 1)]
problem.constraints[:] = "<=0"
problem.function = travel

algorithms = [NSGAII, (NSGAIII, {"divisions_outer":12}), GDE3, SMPSO, SPEA2, (OMOPSO, {"epsilons":[0.05]})]
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
                [s.objectives[1]*(-1) for s in result])
    ax.set_xlabel('$f_1(X):Coste$')
    ax.set_ylabel('$f_2(X):Actividades$')
    ax.set_title(algorithm)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)
plt.show()

# all results together
fig = plt.figure()
plt.grid()

for i, algorithm in enumerate(six.iterkeys(results)):
    result = results[algorithm]["Problem"][0]
    
    plt.plot([s.objectives[0] for s in result],
              [s.objectives[1]*(-1) for s in result], point_type[i], label=algorithm)

plt.xlabel('$f_1(X):Coste$')
plt.ylabel('$f_2(X):Actividades$')
plt.title('Todos los algoritmos')
plt.legend(loc='lower right')
plt.show()

# hypervolume indicator calculator
results = experiment(algorithms, problem, seeds=10, nfe=10000)

algorithms = ['NSGAII',
              'NSGAIII',
              'GDE3',
              'SMPSO',
              'SPEA2',
              'OMOPSO']

hyp = Hypervolume(minimum=[0, -1], maximum=[50, 0])
hyp_result = calculate(results, hyp)
display(hyp_result, ndigits=3)

hyp_results = list()

for algorithm in algorithms:
    hyp_results.append(hyp_result[algorithm]['Problem']['Hypervolume'])

fig = plt.figure()
plt.boxplot(hyp_results, labels = algorithms)
plt.grid()
plt.ylabel('Hypervolume indicator')
plt.show()