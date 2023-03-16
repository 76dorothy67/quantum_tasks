import datetime
import time
import numpy as np


def count_summ(my_number):

    start = datetime.datetime.now()

    try:
        N = int(my_number)
        if 0 <= N <= 10 ** 25:

            result = N

            arr = np.arange(1, N)
            b = np.sum(arr)
            result = N + b

            time.sleep(3)
            print(f"The result is {result}.")

            end = datetime.datetime.now()
            print(f"The execution time is {end - start}")
        else:
            print("The number should be more than 1 and less than 10^25.")

    except ValueError:
        print("Please, enter only a positive integer number.")

    return f"The result is {result}. The execution time is {end - start}"


if __name__ == "__main__":

    my_number = input("Please, enter a positive integer number >> ")
    print(count_summ(my_number))