n_DAAC=int(input())
pares_DAAC=[]
for i_DAAC in range(n_DAAC):
    v_DAAC=int(input())
    if v_DAAC%2==0:
        pares_DAAC.append(v_DAAC)
for x_DAAC in pares_DAAC:
    print(x_DAAC)