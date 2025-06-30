x=int(input())
z=[]
for i in range(x):
    x=input()
    y=list(map(int,x.split()))
    z.append(y)
s=[]    
for i in z:
    d=i[1]-i[0]
    s.append(d)
m=0
for i in s:
    if i>=2:
        m+=1
    
print(m)       
            
        
        
