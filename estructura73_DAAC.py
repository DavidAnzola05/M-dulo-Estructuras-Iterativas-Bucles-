votos_DAAC={'A':0,'B':0,'C':0}
while True:
    print('A B C o FIN')
    v_DAAC=input()
    if v_DAAC=='FIN':
        break
    if v_DAAC in votos_DAAC:
        votos_DAAC[v_DAAC]+=1
for k_DAAC in votos_DAAC:
    print(k_DAAC,votos_DAAC[k_DAAC])