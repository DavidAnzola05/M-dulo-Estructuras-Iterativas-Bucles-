lista_DAAC=[]
n_DAAC=int(input())
for i_DAAC in range(n_DAAC):
    lista_DAAC.append(int(input()))
for x_DAAC in lista_DAAC:
    if x_DAAC%2==0:
        print(x_DAAC)