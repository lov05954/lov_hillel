def dist(Ax, Ay, Bx, By):
    return (((Bx - Ax) ** 2 + (By - Ay) ** 2) ** .5)

Cx = int(input("Введіть координату X центра кільца Cx:"))
Cy = int(input("Введіть координату Y центра кільца Cy:"))

r1 = 2
r2 = 1

while r1 > r2 or r1 == r2:
    r1 = float(input("Введіть внутрішній радіус кільца r1:"))
    r2 = float(input("Введіть зовнішній радіус кільца r2:"))
    if r1 > r2 or r1 == r2:
        print(
            f"""
            !!! Ви припустилися помилки, 
            внутрішній радіус кільця {r1} 
            не може бути більше, ніж зовнішній {r2}
            або дорівнювати йому
            """)

Px = int(input("Введіть координату X точки Px:"))
Py = int(input("Введіть координату X точки Py:"))

if r1 < dist(Cx,Cy,Px,Py) < r2:
    L = "належить"
else: L = "не належить"

print(f"Точка ({Px}, {Py}) {L} кільцю з центром у точці ({Cx}, {Cy}), та r1 = {r1}, r2 = {r2}")