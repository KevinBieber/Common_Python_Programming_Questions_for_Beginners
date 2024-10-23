num=int(input("enter a number:"))
for i in range(2,num+1):
    a = 0
    for j in range(2,i):
        if i%j==0:
            a=1
            break
    if a==1:
        print(f"{i}不是质数")
    else:
        print(f"{i}是质数")