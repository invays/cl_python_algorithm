# https://drive.google.com/file/d/1fLd9r-MJ-tVYHbbM18rTnp31hYZRCSEo/view?usp=sharing

year = int(input("Введите год: "))

if year % 4 != 0:
    print('Невисокосный')
elif year % 100 == 0 and year % 400 == 0:
    print('Високосный')
else:
    print('Високосный')