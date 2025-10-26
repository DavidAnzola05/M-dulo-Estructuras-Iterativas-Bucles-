carrito_DAAC=[]
while True:
    print('1.Agregar 2.Ver 3.Total 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        precio_DAAC=float(input()); carrito_DAAC.append(precio_DAAC)
    elif op_DAAC==2:
        for p_DAAC in carrito_DAAC: print(p_DAAC)
    elif op_DAAC==3:
        print(sum(carrito_DAAC))
    else:
        break