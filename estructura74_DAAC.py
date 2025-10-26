agenda_DAAC={}
while True:
    print('1.Agregar 2.Buscar 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        nom_DAAC=input(); tel_DAAC=input()
        agenda_DAAC[nom_DAAC]=tel_DAAC
    elif op_DAAC==2:
        q_DAAC=input()
        print(agenda_DAAC.get(q_DAAC,'No existe'))
    else:
        break