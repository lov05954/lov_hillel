# Завдання:
#     * згенерувати лист з рандомними числами (числа від 50 до 100 кожне,
#       довжину листа запитати у користувача, але не коротший за 10 та не
#       довший за 50 елементів;
#     * відсортувати елементи в убуваючому порядку (10, 9, 8...)
#     * напечатати на екран
#     * додати можливість циклічного вводу даних для експеріментів
#
#     * ускладнене завдання: написати та використати bubble-sort алгоритм
#
# Підказки:
#     * .sort()
#     * reverse=True

import random
loop = 0
while not(loop):

    nmb = int(input("введіть кількисть випадковіх чисел від 10 до 50: "))
    while nmb < 10 or nmb > 50:
        print("!!!введено число менше 10 або більше 50")
        nmb = int(input("введіть кількисть випадковіх чисел від 10 до 50: "))

    rndm = []
    for _ in range(nmb):
        rndm.append(50+(round(random.random()*100)%50))
    print("\nсгенерована випадкова послідовність:")
    print(rndm)
    rndms = rndm

    #sort
    rndms.sort(reverse=True)
    print("\nвідсортована послідовність в зворотньому напрямку:")
    print(rndms)

    #buble-sort
    for i in range(len(rndm)-1):
        for j in range(i+1, len(rndm)):
            if rndm[i] < rndm[j]:
                tmp = rndm[i]
                rndm[i] = rndm[j]
                rndm[j] = tmp
    print("\nвідсортована послідовність в зворотньому напрямку з використанням buble-sort:")
    print(rndm)

    loop = input("\nдля повторного вводу даних натиснить ENTER"
                 "\nдля виходу введить будь який символ: ")
    if not(loop):
        continue
    break