n_DAAC=int(input())
i_DAAC=1
while i_DAAC<=n_DAAC:
    prod=1
    for j_DAAC in range(1,i_DAAC+1):
        prod*=j_DAAC
    print(prod)
    i_DAAC+=1