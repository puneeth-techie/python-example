#Adding two numbers and printing using format()
num1 = 2.0
num2 = 3.0

sum = num1 + num2
print("Sum of {0} and {1} is: {2}".format(num1,num2,sum))

#Asking two numbers from users
n1 = input('Enter the first number: ')
n2 = input('Enter the second number: ')

# Converting String to integer
print("Sum of the above numbers is: ",int(n1)+int(n2))

#Adding two numbers and printing in single line. Memory efficient
print('The sum is %.1f' %(float(input('Enter the first number: ')) + float(input('Enter the second number: '))))
