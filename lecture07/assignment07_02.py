# Є список (не пайтонівський) чисел (генерований рандомно
# чи заданий вручну) - порахувати унікальні числа у ньому
#
# Наприклад:
#  e 1, 2, 1, 3, 4, 5, 6, 6, 6
#  унікальних 6 (1 повторюється двічі, 6 тричи - три числа не враховуються)
#

L = [1, 2, 1, 3, 4, 5, 6, 6, 6, 8, 89, 89, 9, 6, 0, 6, 0, 1, 111, 111, 0]

S = set(L)

print(f"унікальних: {len(S)} чисел")

for nmu in S:
    n = 0
    for nml in L:
        if nmu == nml:
            n += 1
    if n > 1:
        print(f"число {nmu} повторюється {n} разів")
