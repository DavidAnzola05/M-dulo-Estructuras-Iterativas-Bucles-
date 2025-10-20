def es_primo_DAAC(numero_DAAC):
    if numero_DAAC < 2:
        return False
    for i_DAAC in range(2, int(numero_DAAC ** 0.5) + 1):
        if numero_DAAC % i_DAAC == 0:
            return False
    return True

for n_DAAC in [2, 3, 4, 5, 6, 7, 11, 13, 15, 17]:
    print(f"{n_DAAC} es primo: {es_primo_DAAC(n_DAAC)}")
