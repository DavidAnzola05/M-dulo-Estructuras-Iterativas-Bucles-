n_DAAC=int(input())
contador_DAAC=0
for i_DAAC in range(n_DAAC):
    v_DAAC=int(input())
    if v_DAAC%3==0:
        contador_DAAC+=1
print(contador_DAAC)