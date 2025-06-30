n = int(input()) 
h=[] 
for i in range(n):
    y=input()
    h.append(y.upper())
for i in h:
    if i=='YES':
        print('YES')  
    else:
        print('NO')      
