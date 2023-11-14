import numpy as np


def generate_matrix(n, grid_size=50):

    grid = np.zeros((grid_size, grid_size))
    indices = np.random.choice(grid_size*grid_size, n, replace=False)
    np.put(grid, indices, 1)

    return grid


def save_matrix_to_file(matrix, filename):
    np.savetxt(filename, matrix, fmt='%d', delimiter=',')


def get_user_input():
    return int(input("Введите количество единиц в матрице: "))


n = get_user_input()


matrix = generate_matrix(n)


save_matrix_to_file(matrix, 'matrix.txt')

