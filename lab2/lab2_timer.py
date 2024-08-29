#
#   Author: Catherine Leung
#   This timer file performs a timing of the functions provided in lab2.py
#

import time
import random
import csv
from lab2 import partb_one, partb_two, partb_three

data_sizes = [1000 * i for i in range(1, 11)]  # List of data sizes
results = []

for size in data_sizes:
    my_list = random.sample(range(1, size * 10), size)
    my_list2 = my_list.copy()
    my_list3 = my_list.copy()
    
    target = random.randint(1, size * 10 - 1)
    if target % 2 == 0:
        target += 1

    start_time = time.perf_counter()
    result = partb_one(my_list, target)
    end_time = time.perf_counter()
    time_one = end_time - start_time

    start_time = time.perf_counter()
    result = partb_two(my_list, target)
    end_time = time.perf_counter()
    time_two = end_time - start_time

    start_time = time.perf_counter()
    result = partb_three(my_list, target)
    end_time = time.perf_counter()
    time_three = end_time - start_time

    results.append((size, time_one, time_two, time_three))

with open('timing_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Size", "partb_one", "partb_two", "partb_three"])
    writer.writerows(results)

print("Timing data has been saved to timing_data.csv")
