# Сложение матриц
n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
input()
matrix_b = [list(map(int, input().split())) for _ in range(n)]
matrix_c = [[r + c for r, c in zip(i, j)] for i, j in zip(matrix_a, matrix_b)]

for i in matrix_c:
    print(*i)

# Умножение матриц

# Вариант 1
import numpy as np

n, m = map(int, input().split())
matrix_a = np.array([list(map(int, input().split())) for _ in range(n)])
input()
m, k = map(int, input().split())
matrix_b = np.array([list(map(int, input().split())) for _ in range(m)])

matrix_c = matrix_a.dot(matrix_b)


for i in matrix_c:
    print(*i)

# Вариант 1
n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
input()
m, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]
matrix_c = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for x in range(m):
            matrix_c[i][j] += matrix_a[i][x] * matrix_b[x][j]
for i in matrix_c:
    print(*i)

# Возведение матрицы в степень

# Вариант 1
import numpy as np
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

exp_matrix = np.linalg.matrix_power(matrix, m)

for i in exp_matrix:
    print(*i)

# Вариант 2
n = int(input())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
matrix_b = matrix_a.copy()

while m != 1:
    matrix_c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for x in range(n):
                matrix_c[i][j] += matrix_a[i][x] * matrix_b[x][j]
    matrix_b = matrix_c
    m -= 1
for i in matrix_c:
    print(*i)








