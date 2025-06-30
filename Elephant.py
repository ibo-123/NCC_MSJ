x=int(input())
s=0
while x>0:
    if x>=5:
        s+=1
        x-=5
    elif x>=4:
        s+=1
        x-=4
    elif x>=3:
        s+=1
        x-=3
    elif x>=2:
         s+=1
         x-=2
    else:
        s+=1
        x-=1
print(s)                  
