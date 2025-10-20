def factorial_DAAC(n_DAAC):
    resultado_DAAC = 1
    while n_DAAC > 0:
        resultado_DAAC *= n_DAAC
        n_DAAC -= 1
    return resultado_DAAC

print(factorial_DAAC(5))
