n_DAAC=int(input())
i_DAAC=1
while i_DAAC<=n_DAAC:
    if all(i_DAAC%j_DAAC for j_DAAC in range(2,int(i_DAAC**0.5)+1)) and i_DAAC>1:
        print(i_DAAC)
    i_DAAC+=1