print('Input A')
a = int(input())
print('Input B')
b = int(input())
print ('Initial Square is ',a*b)
i=1
def recurs(a,b,i):

    if a==b:
        print("Recurs has ended with number of ",i)

    elif a>b:
        i=i+1
        a = a - b
        Sq = b*b
        print("Square is", Sq)
        print("A is " + str(b) + ",  B is " +str(b))

        recurs(a,b,i)
    else:
        i=i+1
        b = b-a
        Sq = a*a
        print("Square is", Sq)
        print("A is " + str(a) + ",  B is " + str(a))
        recurs(a,b,i)


recurs(a,b,i)






