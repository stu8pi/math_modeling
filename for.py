for i in 1, 2, 3, 4:
    print(i**2, end='\n') # \n - перевод на новую строку

for i in 1,2,3,4:
    print(i, i**2, sep=' - ')

a=[1,5,7,10]
for i in a:
    print(f'{i}3={i3}')

range # генератор последовательности

# for i in range (1, 1000, 0.01) начало(start), конец(stop), шаг(step) (конец не входит)
b=range(0,10,2)
print(b)
print(type(b))
print(b[3])

c='Good'
for i in range (0,10,1):
    if i<len(c):
        print(c[i]+'-Bad')
    else:
        print(f'{i}'+'-Good')

# break - прерывает цикл  ;  continue - переходит к следующей операции
for i in 'Hello World':
    if i=='o':
        break
    print(i)
    
for i in 'Hello World':
    if i=='o':
        continue
    print(i)