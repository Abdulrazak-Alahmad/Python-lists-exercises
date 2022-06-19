num=0
number= int(input('anything: '))
if number==0:
    print(0)
elif number==1:
    print(1)
else:
    while num<int(number):
        if num==0:
            previous=0
            print(0)
        elif num==1:
            print(1)
            previous=0
            cor=1
        else:
            z=previous
            previous=cor
            cor=z+previous
            print(cor)
        num+=1
