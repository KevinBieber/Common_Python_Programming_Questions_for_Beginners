password1="jianghaoran"
password2="666"
flag=1
for i in range(3):
    if flag==0:
        break
    ans = input("输入密码1")
    if ans==password1:
        ans=input("密码1正确,请输入密码2")
        if ans==password2:
            print("密码2正确，ok了")
            break
        else:
            for j in range(3):
                if j==2:
                    print("没机会了")
                    flag=0
                    break
                ans_=input(f"密码2错误，还有{2-j}次机会")
                if ans_==password2:
                    print("密码正确")
                    break


    else:
        print("密码1错误",end=",")
        print("还有%d次机会"%(2-i))
        if i==2:
            break