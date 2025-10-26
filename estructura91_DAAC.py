lista_DAAC=[int(x) for x in input().split()]
while True:
    print('1.Sumar elemento 2.Ver 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        lista_DAAC.append(int(input()))
    elif op_DAAC==2:
        print(sum(lista_DAAC))
    else:
        break