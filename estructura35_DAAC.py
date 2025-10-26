n_DAAC=int(input())
may_DAAC=None
for i_DAAC in range(n_DAAC):
    v_DAAC=int(input())
    if may_DAAC is None or v_DAAC>may_DAAC:
        may_DAAC=v_DAAC
print(may_DAAC)