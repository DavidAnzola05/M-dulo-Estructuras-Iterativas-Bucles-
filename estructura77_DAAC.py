cola_DAAC=[]
while True:
    print('1.Encolar 2.Desencolar 3.Ver 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        x_DAAC=input(); cola_DAAC.append(x_DAAC)
    elif op_DAAC==2:
        if cola_DAAC: print(cola_DAAC.pop(0))
    elif op_DAAC==3:
        for e_DAAC in cola_DAAC: print(e_DAAC)
    else:
        break