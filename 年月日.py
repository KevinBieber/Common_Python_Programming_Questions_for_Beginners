year,month,day=map(int,input().split())
run=0
mon2=28
day_ans=0
mon1,mon3,mon5,mon7,mon8,mon10,mon12=31,31,31,31,31,31,31
mon4,mon6,mon9,mon11=30,30,30,30
if (year%4==0 and year%100!=0) or year%400==0:
    run=1
else:
    run=0
if run == 0:
    mon2=28
else:
    mon2=29
YEAR=[mon1,mon2,mon3,mon4,mon5,mon6,mon7,mon8,mon9,mon10,mon11,mon12]
for i in range(0,month-1):
    day_ans+=YEAR[i]
day_ans+=day
print(f"这是{year}年的第{day_ans}天")