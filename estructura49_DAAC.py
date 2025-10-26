n_DAAC=int(input())
lista_DAAC=[int(input()) for _ in range(n_DAAC)]
s_DAAC=0
for x_DAAC in lista_DAAC:
    if x_DAAC>10:
        s_DAAC+=x_DAAC
print(s_DAAC)