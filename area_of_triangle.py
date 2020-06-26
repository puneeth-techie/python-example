#Calculating the area of triangle

#Taking the inputs from the user

a = float(input('Enter the value of side a: '))
b = float(input('Enter the value of side b: '))
c = float(input('Enter the value of side c: '))

#Calculating the semi-perimeter
s = (a + b + c)/2

#Calculate the area of triangle now
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of Triangle is: %.2f'%area)
