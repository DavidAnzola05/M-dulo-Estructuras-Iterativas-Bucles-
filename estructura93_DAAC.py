tienda_DAAC={}
while True:
    print('1.Ingresar 2.Vender 3.Listar 4.Salir')
    op_DAAC=int(input())
    if op_DAAC==1:
        n_DAAC=input();p_DAAC=float(input());tienda_DAAC[n_DAAC]=[p_DAAC,0]
    elif op_DAAC==2:
        n_DAAC=input();q_DAAC=int(input())
        if n_DAAC in tienda_DAAC:
            tienda_DAAC[n_DAAC][1]+=q_DAAC
    elif op_DAAC==3:
        for k_DAAC,v_DAAC in tienda_DAAC.items(): print(k_DAAC,v_DAAC)
    else:
        break