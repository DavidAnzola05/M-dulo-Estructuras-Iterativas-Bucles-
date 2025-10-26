productos_DAAC={}
while True:
    print('1.Agregar 2.Listar 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        nombre_DAAC=input(); precio_DAAC=float(input())
        productos_DAAC[nombre_DAAC]=precio_DAAC
    elif op_DAAC==2:
        for k_DAAC,v_DAAC in productos_DAAC.items():
            print(k_DAAC,v_DAAC)
    else:
        break