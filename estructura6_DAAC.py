a_DAAC=int(input())
s_DAAC=0
while a_DAAC>0:
    s_DAAC+=a_DAAC%10
    a_DAAC//=10
print(s_DAAC)