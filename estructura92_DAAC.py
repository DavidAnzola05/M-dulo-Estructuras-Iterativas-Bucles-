muro_DAAC=[]
while True:
    print('1.Publicar 2.Ver 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        muro_DAAC.append(input())
    elif op_DAAC==2:
        for p_DAAC in muro_DAAC: print(p_DAAC)
    else:
        break