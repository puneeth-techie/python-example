#Calculate the square root of the number

#Importing cmath module for complex numbers
import cmath


#This entered value is in String
num = input('Enter a number: ')

#Converting num to number
num_sqrt = float(num) ** 0.5

print('The square root of %0.3f is %0.3f'%(float(num),num_sqrt))

#eval is the method used to take an argument which is in a form of expression
n = eval(input('Enter the complex number: '))


n_sqrt = cmath.sqrt(n)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(n,n_sqrt.real,n_sqrt.imag))
