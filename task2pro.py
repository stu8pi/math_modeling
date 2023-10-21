a, b, c  = int(input()), int(input()), int(input())
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    if a == b == c:
        x = 'равносторонний'
    elif (a == b and a != c) or (a != b and a == c) or (b == c and b != a):
        x = 'равнобедренный'
    else:
        x = 'разносторонний'
    print(f'Существует, {x}')
else:
    print('Не существует')