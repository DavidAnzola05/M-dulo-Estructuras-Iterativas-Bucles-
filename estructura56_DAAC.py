n_DAAC=int(input())
for i_DAAC in range(1,n_DAAC+1):
    s=0
    for j_DAAC in range(1,i_DAAC+1):
        s+=j_DAAC
    print(s)