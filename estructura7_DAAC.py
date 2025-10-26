a_DAAC=int(input())
c_DAAC=0
for i_DAAC in range(1,a_DAAC+1):
    if a_DAAC%i_DAAC==0:
        c_DAAC+=1
print('Divisores:',c_DAAC)