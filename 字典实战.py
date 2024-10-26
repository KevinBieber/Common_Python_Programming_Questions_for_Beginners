a,b=map(int,input().split())
dictA={"0":0}
trans=""
num="0"
trans_ans=[]
for i in range(a):
    trans,num=input().split()
    num=int(num)
    if trans in dictA:
        num=dictA[trans]+num
    dictA.update({trans:num})
for i in range(b):
    trans_ans.append(input())
for i in trans_ans:
    if i not in dictA:
        print(0)
    else:
        print(dictA[i])