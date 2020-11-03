# https://drive.google.com/file/d/1L9QXF0INyW4kqI1ajcb_S-YJMwI_sQnK/view?usp=sharing
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if c < a < b or b < a < c:
    med = a
elif c < b < a or a < b < c:
    med = b
else:
    med = c

print(med)