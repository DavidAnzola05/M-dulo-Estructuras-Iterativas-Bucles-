n_DAAC=int(input())
men_DAAC=None
for i_DAAC in range(n_DAAC):
    v_DAAC=int(input())
    if men_DAAC is None or v_DAAC<men_DAAC:
        men_DAAC=v_DAAC
print(men_DAAC)