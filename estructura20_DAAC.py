a_DAAC=int(input())
count_DAAC=0
for i_DAAC in range(1,a_DAAC+1):
    if a_DAAC%i_DAAC==0:
        count_DAAC+=1
print('Primo' if count_DAAC==2 else 'No primo')