n_DAAC=int(input())
c_DAAC=0
for i_DAAC in range(1,n_DAAC+1):
    if i_DAAC%4==0:
        c_DAAC+=1
print(c_DAAC)