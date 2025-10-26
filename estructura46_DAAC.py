n_DAAC=int(input())
pares=0;impares=0
for i_DAAC in range(n_DAAC):
    v_DAAC=int(input())
    if v_DAAC%2==0: pares+=1
    else: impares+=1
print(pares,impares)