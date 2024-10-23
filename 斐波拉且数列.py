num1 = 1
num2 = 1
c = 0
a = int(input("enter a num>=3 :"))
if a == 1:
    print(num1)
if a == 2:
    print(num2)
if a >= 3:
    for i in range(a-2):
        c = num1+num2
        num1 = num2
        num2 = c
    print(c)