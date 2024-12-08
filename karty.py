import numpy as np

length = 99
final_median = 50
final_mean = 45
final_range = 99
start_value = 1

while True:
    num_array = np.random.randint(start_value, start_value + final_range, length)
    
    num_array[length-1] = start_value + final_range
    
    current_mean = np.mean(num_array)
    adjustment = final_mean - current_mean
    num_array = np.round(num_array + adjustment).astype(int)
    
    num_array = np.clip(num_array, start_value, start_value + final_range)
    
    #median
    current_median = np.median(num_array)
    if current_median != final_median:
        diff = int(final_median - current_median)
        num_array = np.sort(num_array)
        mid_index = length // 2
        num_array[mid_index:] += diff

    #kontrola
    num_array = np.clip(num_array, start_value, start_value + final_range)
    
    num_array[length-1] = start_value + final_range
    
    num_array = np.sort(num_array)
    
    #check
    if np.median(num_array) == final_median and np.mean(num_array) == final_mean:
        break

print(num_array)