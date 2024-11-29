# MultiProcessing with ProcessPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time

def Print_numbers(numbers):
    time.sleep(1)
    return f"Number: {numbers * numbers}"

numbers = [1,2,3,4,5]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(Print_numbers, numbers)

    for result in results:
        print(result)