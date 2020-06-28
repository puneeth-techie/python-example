#Converting Celsius to Fahrenheit
#Formula Fahrenheit = (Celsius * 1.8) + 32

Celsius = float(input('Enter the Celsius: '))

Fahrenheit = (Celsius * 1.8) + 32
print('%0.2f Celsius is equal to %0.2f Fahrenheit\n'%(Celsius, Fahrenheit))

#Converting Fahrenheit to Celsius
#Formula Celsius = (Fahrenheit - 32) / 1.8

Fahrenheit = float(input('Enter the Fahrenheit value: '))

Celsius = (Fahrenheit - 32) / 1.8
print('%0.2f Fahrenheit is equal to %0.2f Farhenheit'%(Fahrenheit, Celsius))
