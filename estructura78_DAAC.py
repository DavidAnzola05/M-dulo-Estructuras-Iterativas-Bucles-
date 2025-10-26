inventario_DAAC={'manzana':10,'banana':5}
while True:
    print('1.Comprar 2.Vender 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        item_DAAC=input(); cantidad_DAAC=int(input())
        inventario_DAAC[item_DAAC]=inventario_DAAC.get(item_DAAC,0)+cantidad_DAAC
    elif op_DAAC==2:
        item_DAAC=input(); cantidad_DAAC=int(input())
        if inventario_DAAC.get(item_DAAC,0)>=cantidad_DAAC:
            inventario_DAAC[item_DAAC]-=cantidad_DAAC
        else:
            print('No suficiente') 
    else:
        break