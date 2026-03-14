def calculate_average(numbers):

    total = 0

    for n in numbers:
        total += n

    avg = total / len(numbers)

    return avg


print(calculate_average([10,20,30]))