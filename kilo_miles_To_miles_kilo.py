#Calculating kilometers to miles

kilo = float(input('Enter the kilometer: '))

conv_factor = 0.621371

#Calculate miles
miles = kilo * conv_factor

print('%0.2f kilometers is equal to %0.2f miles\n'%(kilo, miles))

#Taking input from user
miles = float(input('Enter the miles: '))

#Converting miles to kilometers
kilometers = miles / conv_factor

print('%0.2f miles is equal to %0.2f kilometers'%(miles, kilometers))



