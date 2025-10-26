n_DAAC=int(input())
s_DAAC=0
for i_DAAC in range(n_DAAC):
    x_DAAC=int(input())
    s_DAAC+=x_DAAC
print(s_DAAC/n_DAAC if n_DAAC>0 else 0)