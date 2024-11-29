# MultiThreading with ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time

def Print_numbers(numbers):
    time.sleep(1)
    return f"Number: {numbers}"

numbers = [1,2,3,4,5,5,2,5,8,9,4,4,4]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(Print_numbers, numbers)

for result in results:
    print(result)