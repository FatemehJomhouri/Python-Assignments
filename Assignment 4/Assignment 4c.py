num= int(input('input number of components:D :  '))

if num==1 :
    print(f'Fibonachi: 1 ')

else :
    print('Fibonachi: 1 ', end=' ')
    i=1
    j=0
    for x in range(2, num):

        sum= j + i
        j = i
        i = sum
        print(sum, end='  ')