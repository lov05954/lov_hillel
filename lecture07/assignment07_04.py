# Згенерувати, за допомогою list comprehension,
# квадратну диагональну матрицю завданої розмірності (N)
# N - запитати у користувача
#
# Приклад:
# N = 4
#
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
# підказка: j+1 if i = j else 0
#


N = int(input("введіть розмірность матриці:"))

l = [[j+1 if i==j else 0 for j in range(N)] for i in range(N)]

for i in range(N):
    print(l[i])