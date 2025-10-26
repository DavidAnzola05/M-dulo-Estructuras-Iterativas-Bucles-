registro_DAAC=[]
while True:
    print('1.Alta 2.Listar 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        registro_DAAC.append(input())
    elif op_DAAC==2:
        for r_DAAC in registro_DAAC: print(r_DAAC)
    else:
        break