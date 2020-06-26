#Calculating standard form of Quadratic Equation
#Formula to find out standard QE is (-b(+or-)sqrt(b**2-4ac))/2a

# ax**2 + bx + c = 0, where a,b and c are real numbers and a != 0

#import complex math module
import cmath

a = float(input('Enter the number a: '))
b = float(input('Enter the number b: '))
c = float(input('Enter the number c: '))

#Calculate the discriminant
dis = (b**2)-(4*a*c)

#find two solutions '+' and '-'
solu_1 = ((-b + cmath.sqrt(dis))/2*a)
solu_2 = ((-b - cmath.sqrt(dis))/2*a)

print('The solution for the given quadratic equation are {0} and {1}'.format(solu_1,solu_2))
