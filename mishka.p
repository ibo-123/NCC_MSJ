num=int(input())
count_m=0
count_c=0
for i in range(num):
    m,c=map(int,input().split())
    if m>c:
        count_m+=1
    elif c>m:
        count_c+=1
if count_m>count_c:
    print("Mishka")
elif count_m<count_c:
    print("Chris")
else:
    print("Friendship is magic!^^")
