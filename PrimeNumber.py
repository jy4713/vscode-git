
first = input("first number : ")
second = input("second number : ")
numRange = range(int(first),int(second))

for num in numRange:
    nonPrime=[]
    for divideNum in range(2,num-1):
        if num%divideNum==0 :
#            print('{0} - {1}'.format(num, divideNum),end='.\n')
            nonPrime.append(divideNum);
    if len(nonPrime) == 0:
        print('Prime Number : {0}'.format(str(num)))
    else:
#       print('{0}'.format(str(num)),end=' : ')
        for divNum in nonPrime:
            pass;
#           print('{0}'.format(str(divNum)),end=' ')
#       print('')
