a_DAAC=int(input())
b_DAAC=int(input())
c_DAAC=0
for i_DAAC in range(a_DAAC,b_DAAC+1):
    if i_DAAC%2!=0:
        c_DAAC+=1
print(c_DAAC)