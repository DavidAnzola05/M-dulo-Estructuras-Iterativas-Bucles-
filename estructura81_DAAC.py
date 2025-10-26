lista_DAAC=[]
while True:
    print('1.Agregar 2.Ordenar 3.Ver 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        lista_DAAC.append(int(input()))
    elif op_DAAC==2:
        lista_DAAC.sort()
    elif op_DAAC==3:
        for x_DAAC in lista_DAAC: print(x_DAAC)
    else:
        break