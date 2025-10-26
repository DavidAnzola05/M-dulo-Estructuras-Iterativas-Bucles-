a_DAAC=int(input())
b_DAAC=0
for i_DAAC in range(1,a_DAAC+1):
    if i_DAAC%3==0:
        b_DAAC+=i_DAAC
print(b_DAAC)