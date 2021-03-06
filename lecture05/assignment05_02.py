# Завдання:
#    * запитати у користувача речення на вхід (пуста строка не приймається);
#    * відсортувати літери у кожному слові
#    * вивести результат на екран
#    * дозвольте користувачу вводити дані декілька разім (не безкінечне)
#
#    * ускладнене завдання: відсортуйте слова між собою (не тільки літери у словах),
#                           у спадаючому/зростаючому порядку -
#
#    * для саморозвитку: використайте tuple/set для зберігання літер у словах.
#                        що як убрати сортування літер у словах. чи будуть питання?
#
# Підказки:
#    * str.split()
#    * list(sequence), а також tuple/set конструктори
#    * reverse=True


loop = 0
while not loop:

    txt = input("введіть речення:")
    while len(txt) == 0:
        print("!!!введено ")
        txt = input("введіть речення:")

    txts = []
    for wrd in txt.split():
        wrd = sorted(wrd)
        wrd = ''.join(wrd)
        #print(wrd)
        txts.append(wrd)
    txts = ' '.join(txts)
    print("\nвідсортовані літери у кожному слові:")
    print(txts)

    txts = sorted(txts.split())
    txts = ' '.join(txts)
    print("\nвідсортовані слова у реченні:")
    print(txts)

    txts = sorted(txts.split(), reverse=True)
    txts = ' '.join(txts)
    print("\nвідсортовані слова у реченні у зворотньому напрямку:")
    print(txts)

    loop = input("\nдля повторного вводу даних натиснить ENTER"
                 "\nдля виходу введить будь який символ: ")
    if not loop:
        continue
    break