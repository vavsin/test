a = int(input('enter the initial number '))
z = int(input('enter the final number '))
for i in range(a, z + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                #print(i, 'is not prime')
                break
            else:
                print(i)
