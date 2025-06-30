x=int(input())
h=[]
for i in range(x):
    y=input()
    l=0
    r=0
    for j in range(3):
        l+=int(y[j])
    for k in [5,4,3]:
        r+=int(y[k]) 
    if l==r:
        h.append('YES')
    else:
        h.append('NO')    
for i in h:
    print(i)
