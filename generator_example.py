numbers = [1,2,3,4,5]

def square_number(numbers):
    square_value = []
    for num in numbers:
        square_value.append(num * num)

    return square_value

result = square_number(numbers)
print(result)

def square_generator(numbers):
    for num in numbers:
        yield (num*num)

result_gn = square_generator(numbers)
print(list(result_gn))
