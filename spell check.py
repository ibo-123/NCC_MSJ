x=int(input())
h=[]
for i in range(x):
    y=int(input())
    z=input()
    if len(z)!=len(set(z)):
            print("NO")
            continue
    l="Timur"
    if len(l)==len(z):
            for j in l:
                    if j not in z:
                            print("NO")
                            break
            else:
                 print("YES")
    else:
            print("NO")
