a_DAAC=int(input())
for i_DAAC in range(1,a_DAAC+1):
    if i_DAAC%3==0 and i_DAAC%5==0:
        print('FizzBuzz')
    elif i_DAAC%3==0:
        print('Fizz')
    elif i_DAAC%5==0:
        print('Buzz')
    else:
        print(i_DAAC)