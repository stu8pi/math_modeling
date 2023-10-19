a = int(input())
b = int(input())
if b == 0:
    print('На ноль делить нельзя.')
elif a % b == 0:
    d = a // b
    print(f'{a} делится на {b}. Частное: {d}')
else:
    c = a % b
    d = a // b
    print(f'{a} не делится на {b}. Частное: {c}. Остаток: {d}')