opcion_DAAC=0
while opcion_DAAC!=3:
    print('1.Sumar 2.Restar 3.Salir')
    opcion_DAAC=int(input())
    if opcion_DAAC==1:
        a_DAAC=int(input());b_DAAC=int(input())
        print(a_DAAC+b_DAAC)
    elif opcion_DAAC==2:
        a_DAAC=int(input());b_DAAC=int(input())
        print(a_DAAC-b_DAAC)