n_DAAC=int(input())
s_DAAC=0
for i_DAAC in range(1,n_DAAC+1):
    if i_DAAC%5==0:
        s_DAAC+=i_DAAC
print(s_DAAC)