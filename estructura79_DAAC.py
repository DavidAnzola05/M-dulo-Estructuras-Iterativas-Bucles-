usuarios_DAAC={}
while True:
    print('1.Registrar 2.Login 3.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        u_DAAC=input(); p_DAAC=input()
        usuarios_DAAC[u_DAAC]=p_DAAC
    elif op_DAAC==2:
        u_DAAC=input(); p_DAAC=input()
        if usuarios_DAAC.get(u_DAAC)==p_DAAC:
            print('Bienvenido')
        else:
            print('Incorrecto')
    else:
        break