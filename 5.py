print("Tabla de multiplicar del 1 al 10:")
print("-" * 40)

for i_DAAC in range(1, 11):
    for j_DAAC in range(1, 11):
        print(f"{i_DAAC * j_DAAC:4}", end="")
    print()
