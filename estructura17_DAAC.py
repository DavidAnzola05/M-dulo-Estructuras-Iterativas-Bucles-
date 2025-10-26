a_DAAC=int(input())
bin_DAAC=''
while a_DAAC>0:
    bin_DAAC=str(a_DAAC%2)+bin_DAAC
    a_DAAC//=2
print(bin_DAAC if bin_DAAC!='' else '0')