historial_DAAC=[]
while True:
    print('1.Insertar 2.Buscar 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        historial_DAAC.append(input())
    elif op_DAAC==2:
        q_DAAC=input()
        for e_DAAC in historial_DAAC:
            if q_DAAC in e_DAAC: print(e_DAAC)
    else:
        break