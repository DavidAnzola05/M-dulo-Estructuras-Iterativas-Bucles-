agenda_DAAC={}
while True:
    print('1.Agregar 2.Eliminar 3.Ver 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        n_DAAC=input();t_DAAC=input();agenda_DAAC[n_DAAC]=t_DAAC
    elif op_DAAC==2:
        n_DAAC=input();agenda_DAAC.pop(n_DAAC,None)
    elif op_DAAC==3:
        for k_DAAC,v_DAAC in agenda_DAAC.items(): print(k_DAAC,v_DAAC)
    else:
        break