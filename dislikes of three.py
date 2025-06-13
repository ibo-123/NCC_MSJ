polycurp=[]
polycurp_num=1
polycurp_str="1"
for i in range(2000):
    if polycurp_num%3!=0 and polycurp_str[-1]!="3":
        polycurp.append(polycurp_num)
    polycurp_num+=1
    polycurp_str=polycurp_num
    polycurp_str=str(polycurp_str)
num_test=int(input())
for i in range(num_test):
    k=int(input())
    print(polycurp[k-1])
    
