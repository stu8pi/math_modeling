n = int(input())
num1 = 0
num2 = 1
for i in range(n+1):
    num2 = num1 + num2
    num1 = num2 - num1
    print(num1, end = ' ')