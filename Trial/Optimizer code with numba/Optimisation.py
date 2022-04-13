from Algorithms import Bat_Algorithm
from Functions import Ackley

fn= Ackley()
optimiser= Bat_Algorithm(fn, Population_Size=500, Num_Movements=200)
                         
#%time _ = optimiser.Run(fn)

print('-'*40)
print("Optimiser")
print('-'*40)
print('Best Fitness: %.5f' %(optimiser.Best_Fitness))
print('Best Position: x: %.05f, y: %.5f' %(optimiser.Best_Position[0,0]), (optimiser.Best_Position[0,1]))
print('-'*40)
print("Function")
print('-'*40)
print('Global Minimum: %.5f' % (fn.minima))
print('Location x: %.5f' % (fn.location[0,0], fn.location[0,1]))
print('-'*40)
