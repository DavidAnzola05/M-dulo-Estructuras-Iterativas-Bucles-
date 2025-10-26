lista_DAAC=[]
n_DAAC=int(input())
for i_DAAC in range(n_DAAC):
    lista_DAAC.append(int(input()))
s_DAAC=0
for x_DAAC in lista_DAAC:
    s_DAAC+=x_DAAC
print(s_DAAC)