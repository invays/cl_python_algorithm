# https://drive.google.com/file/d/1l9U5aNp0spRP8pDfPdP3zcPpljj5gkrX/view?usp=sharing

user_input = int(input("Введите трехзначное число: "))
a = user_input // 100
b = user_input % 100 // 10
c = user_input % 10

summa = a + b + c
multp = a * b * c

print(f'Cумма цифр трехзначного числа {summa}')
print(f'Произведение цифр трехзначного числа {multp}')