saldo_DAAC=0
while True:
    print('1.Aumentar 2.Disminuir 3.Ver 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        saldo_DAAC+=int(input())
    elif op_DAAC==2:
        saldo_DAAC-=int(input())
    elif op_DAAC==3:
        print(saldo_DAAC)
    else:
        break