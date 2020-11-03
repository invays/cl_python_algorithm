# https://drive.google.com/file/d/1p0NjEVr8jW1ie1VMEwMXgLuHRd3jzPvz/view?usp=sharing

x1 = int(input("Первая координата x1: "))
y1 = int(input("Первая координа y1: "))
x2 = int(input("Вторая координата x2: "))
y2 = int(input("Вторая координата y2: "))

k = (y2 - y1)/(x2 - x1)
b = y1 - k * x1

print(f'y = {k}x + {b}')
