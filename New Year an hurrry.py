x=input()
y=list(map(int,x.split()))
l=y[1]
m=0
for i in range(1,y[0]+1):
    if (l+i*5)<=240:
        m+=1
        l+=i*5
    else:
        break
       
print(m)
