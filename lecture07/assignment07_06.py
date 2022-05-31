# Переписати цикл з використанням iter/next функцій
# підказка: idx, s[idx]
#s = "Hello world!"
# idx = 0
# while True:
#     ch = s[idx]
#     if ch == ' ':
#         break
#     print(ch, end="")
#     idx += 1
# print()

s = "Hello world!"
it = iter(s)
while True:
    ch = next(it)
    if ch == ' ':
        break
    print(ch, end="")
print()