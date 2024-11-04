import numpy as num

lenght = 99
start = 1
final_median = 24
final_middle = 23
final_range = 100

def generate(start, lenght, current_sequence, final_median, final_middle, final_range):
    if len(current_sequence) == lenght:

        median, middle, rangeTemp = compute_statistics(current_sequence)

        if (num.isclose(median, final_median) and num.isclose(middle, final_middle) and num.isclose(rangeTemp, final_range)):
            return current_sequence
        return None

    
    for next_value in range(start, start + 100):
        result = generate(next_value + 1, lenght, current_sequence + [next_value], final_median, final_middle, final_range)
        if result:
            return result
    return None

def compute_statistics(test):
    median = num.median(test)
    middle = num.mean(test)
    rangeTemp = max(test) - min(test)
    return median, middle, rangeTemp
print("skibi")
solution = generate(start, lenght, [], final_median, final_middle, final_range)
print(solution)
