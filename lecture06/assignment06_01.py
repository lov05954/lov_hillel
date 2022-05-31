# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.

#s = "aaa dsds aaa ccc aaa bbb ddd dsds ccc dsds ccc cccc"

s = input("введіть речення:")

cntW = {}
cntL = {}

for w in s.split(): # words
    n = 1
    if w in cntW:
        n = cntW[w]
        n += 1
    cntW[w] = n

    for l in w: # liters
        m = 0
        if l in cntL:
            m = cntL[l]
        if l in w:
            m += 1
        cntL[l] = m

print("\nкількість слів у реченні:")
print(cntW)
print("\nкількість букв у реченні:")
print(cntL)