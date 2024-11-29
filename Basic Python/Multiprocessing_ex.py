import multiprocessing
import time
import math
import sys

sys.set_int_max_str_digits(100000)

def count_fact(number):
    print(f"Fcatorial of number {number} :")
    result = math.factorial(number)
    print(f"{result}")
    return result

if __name__ == '__main__':
    numbers = [1000, 6000, 700]

    st = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.map(count_fact, numbers)

    et = time.time()

    print(et-st)
