historial_DAAC=[]
while True:
    print('1.Push 2.Pop 3.Ver 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        x_DAAC=input(); historial_DAAC.append(x_DAAC)
    elif op_DAAC==2:
        if historial_DAAC: print(historial_DAAC.pop())
    elif op_DAAC==3:
        for e_DAAC in historial_DAAC: print(e_DAAC)
    else:
        break