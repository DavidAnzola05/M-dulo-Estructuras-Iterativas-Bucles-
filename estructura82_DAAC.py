matriz_DAAC=[]
filas_DAAC=int(input());col_DAAC=int(input())
for i_DAAC in range(filas_DAAC):
    fila_DAAC=[]
    for j_DAAC in range(col_DAAC):
        fila_DAAC.append(int(input()))
    matriz_DAAC.append(fila_DAAC)
suma_DAAC=0
for f_DAAC in matriz_DAAC:
    for v_DAAC in f_DAAC:
        suma_DAAC+=v_DAAC
print(suma_DAAC)