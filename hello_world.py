import os
import sys
import cmath
import math


print(' Hello, World!' )
print('\n')
print('\x1b[38;2;5;86;243m' + 'Hello in blue' + '\x1b[0m')
print('\n')
print('Where Am I : ' + os.path.dirname(sys.executable))

#  Quadraitcas
a = 2
b = 25
c = 75

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('\n\n{0}x^2 + {1}x + {2} :'.format(a,b,c))
print('The solution are {0} and {1}'.format(sol1,sol2))

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('{0}x^2 + {1}x + {2} :'.format(a,b,c))
print('The solution are {0} and {1}'.format(sol1,sol2))

print('\n')
print('Numeros primos del 1 al 100')
for num in range(2,101):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
       print (num,end=' ')