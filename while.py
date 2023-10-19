# while  переменная цикла
# while <переменная> <условие>:
    # <инструкция>
i = 5
while i<15:
    i +=2
    print(i**2)
    print('i', i)
    
# break - прерывает цикл  ;  continue - переходит к следующей операции
for i in 'Hello World':
    if i=='o':
        break
    print(i)
    
for i in 'Hello World':
    if i=='o':
        continue
    print(i)