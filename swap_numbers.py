#Swap Two Numbers

x = float(input('Enter the value of x: '))
y = float(input('Enter the value of y: '))

temp = x
x = y
y = temp

print('The value of x is {0} and y is {1}'.format(int(x),int(y)))
