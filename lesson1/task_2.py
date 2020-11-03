# https://drive.google.com/file/d/1p0NjEVr8jW1ie1VMEwMXgLuHRd3jzPvz/view?usp=sharing

a = 5
b = 6

bit_and = bin(a&b)
bit_or = bin(a|b)
bit_or2 = bin(a^b)
bit_left = bin(a << 2)
bit_rigth = bin(a >> 2)

print(f'Бинарный логический оператор И = {bit_and}\n'
      f'Бинарный логический оператор ИЛИ = {bit_or}\n'
      f'Бинарный логический оператор Исключительное ИЛИ = {bit_or2}\n'
      f'Операция над числом 5 побитовый сдвиг влево = {bit_left}\n'
      f'Операция над числом 5 побитовый сдвиг вправо = {bit_rigth}\n')
