num = int(input())
for i in range(2, num+1):
    if num % i == 0:
        flag = True
        for k in range(2, i):
            if i % k == 0:
                flag = False
                break
        if flag == True:
            print(i)  