num1 = int(input())
x = num1 % 10
num2 = x
num1 = num1 // 10
while num1 > 0:
    x = num1 % 10
    num1 = num1 // 10
    num2 *= 10
    num2 += x
print(num2)