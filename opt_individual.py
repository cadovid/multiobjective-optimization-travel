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

# select desired algorithm and number of evaluations
algorithm = NSGAII(problem)
algorithm.run(10000)

# display the results
for solution in algorithm.result:
    print(solution.objectives)
    print(solution.variables)

# plot the results using matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
plt.scatter([s.objectives[0] for s in algorithm.result],
            [s.objectives[1]*(-1) for s in algorithm.result])
plt.xlim([0, 50])
plt.ylim([-0.5, 1.5])
plt.xlabel('$f_1(X):Coste$')
plt.ylabel('$f_2(X):Actividades$')
plt.title('Travel Function Pareto Front')
plt.show()

# plot all variables using matplotlib, one subplot per variable
fig = plt.figure()

for i in range(0,3):
    
    ax = fig.add_subplot(1, 3, i+1, projection='3d')
    ax.set_axisbelow(True)
    ax.grid()
    ax.scatter([s.variables[i] for s in algorithm.result],
            [s.objectives[0] for s in algorithm.result],
            [s.objectives[1]*(-1) for s in algorithm.result])
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 50])
    ax.set_zlim([0, 1])
    ax.view_init(elev=25.0, azim=100.0)
    ax.set_xlabel('$Variable x$'+str(i+1))
    ax.set_ylabel('$f_1(X):Coste$')
    ax.set_zlabel('$f_2(X):Actividades$')
    ax.set_title('Travel Function Variable x'+str(i+1)+' Value')
    
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)
plt.show()

# plot all the variables using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([s.variables[0] for s in algorithm.result],
            [s.variables[1] for s in algorithm.result],
            [s.variables[2] for s in algorithm.result])
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])
ax.view_init(elev=30.0, azim=130.0)
ax.set_xlabel('$Variable x1$')
ax.set_ylabel('$Variable x2$')
ax.set_zlabel('$Variable x3$')
ax.set_title('Travel Function All Variable Value')
plt.show()
