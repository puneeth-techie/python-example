#Calculating whether the given year is leap year or not]

year = int(input('Enter the year \'yyyy\': '))

if(year % 4 == 0):
    print('{} is Leap Year'.format(str(year)))
elif(year % 100 == 0 and year % 400 == 0):
    print('{} is Leap Year'.format(str(year)))
else:
    print('{} is not a Leap Year'.format(str(year)))
