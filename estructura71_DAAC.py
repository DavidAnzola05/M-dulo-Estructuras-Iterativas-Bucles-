saldo_DAAC=0
while True:
    print('1.Depositar 2.Retirar 3.Saldo 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        x_DAAC=float(input()); saldo_DAAC+=x_DAAC
    elif op_DAAC==2:
        x_DAAC=float(input())
        if x_DAAC<=saldo_DAAC:
            saldo_DAAC-=x_DAAC
        else:
            print('Fondos insuficientes')
    elif op_DAAC==3:
        print(saldo_DAAC)
    else:
        break