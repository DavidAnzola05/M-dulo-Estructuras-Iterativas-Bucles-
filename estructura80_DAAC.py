saldo_DAAC=1000
while True:
    print('1.Retirar 2.Saldo 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        x_DAAC=int(input())
        if x_DAAC<=saldo_DAAC: saldo_DAAC-=x_DAAC
        else: print('No hay dinero')
    elif op_DAAC==2:
        print(saldo_DAAC)
    else:
        break