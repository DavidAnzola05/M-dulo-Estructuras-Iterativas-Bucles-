productos_DAAC={}
while True:
    print('1.Ingresar 2.Comprar 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        p_DAAC=input();pr_DAAC=float(input());productos_DAAC[p_DAAC]=pr_DAAC
    elif op_DAAC==2:
        p_DAAC=input();q_DAAC=int(input())
        if p_DAAC in productos_DAAC:
            print('Total',productos_DAAC[p_DAAC]*q_DAAC)
    else:
        break