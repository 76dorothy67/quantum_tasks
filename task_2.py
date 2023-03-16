import numpy as np


def count_islands(m, n, matrix):

    count_island = 0
    ix = 0
    iy = 0

    for ix, iy in np.ndindex(matrix.shape):
        if matrix[ix, iy] == 1:
            count_island += 1
            matrix[ix, iy] = count_island + 1
            fill_island(count_island + 1)

    return f"The count of islands is {count_island}"


def fill_island(number):

    while True:
        count = 0
        ended = True
        for ix, iy in np.ndindex(matrix.shape):
            if matrix[ix, iy] == 1:

                if iy >= 1 and matrix[ix, iy - 1] == number:
                    matrix[ix, iy] = number
                    ended = False
                if iy < n - 1 and matrix[ix, iy + 1] == number:
                    matrix[ix, iy] = number
                    ended = False
                if ix >= 1 and matrix[ix - 1, iy] == number:
                    matrix[ix, iy] = number
                    ended = False
                if ix < m - 1 and matrix[ix + 1, iy] == number:
                    matrix[ix, iy] = number
                    ended = False
        if ended is True:
            break


if __name__ == "__main__":

    # друге завдання

    try:

        m = int(input("Please, enter a number of rows >> "))
        n = int(input("Please, enter a number of columns >> "))

        matrix_list = np.zeros(m * n)

        item = 0
        while item < m * n:
            try:
                number = int(input("Please enter 1 to set the island or 0 to set the ocean >> "))

                if number == 1 or number == 0:

                    matrix_list[item] = number
                    item += 1

                else:
                    print("Please enter only 1 or 0.")

            except ValueError:
                print("Please use only numbers.")

        matrix = matrix_list.reshape(m, n)

        print(count_islands(m, n, matrix))
    except ValueError:
        print("Please enter only numbers.")