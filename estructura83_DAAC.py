menu_DAAC=0
while menu_DAAC!=4:
    print('1.A 2.B 3.C 4.Salir')
    menu_DAAC=int(input())
    if menu_DAAC==1:
        x_DAAC=int(input());print(x_DAAC*2)
    elif menu_DAAC==2:
        x_DAAC=int(input());print(x_DAAC*3)
    elif menu_DAAC==3:
        x_DAAC=int(input());print(x_DAAC*4)