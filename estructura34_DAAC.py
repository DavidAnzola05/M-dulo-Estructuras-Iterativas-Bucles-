total_DAAC=0
n_DAAC=int(input())
for i_DAAC in range(n_DAAC):
    precio_DAAC=float(input());cantidad_DAAC=int(input())
    total_DAAC+=precio_DAAC*cantidad_DAAC
print(total_DAAC)