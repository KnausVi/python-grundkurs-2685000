def square_of_sum(number):
    sum_of_numbers = 0
    for item in range(number+1):
        sum_of_numbers += item
    return sum_of_numbers **2

def sum_of_squares(number):
    result_sum_of_squares = 0
    for item in range(number+1):
        result_sum_of_squares += item **2
    return result_sum_of_squares

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
