lista_DAAC=[int(x) for x in input().split()]
suma_DAAC=0
for x_DAAC in lista_DAAC:
    if x_DAAC%2==0: suma_DAAC+=x_DAAC
print(suma_DAAC)