a=str(input())
p=int(input())
if a=='����':
    if p%100==11 or p%100==12 or p%100==13 or p%100==14 or p-100==11 or p-100==12 or p-100==13 or p-100==14:
         print(p,'������')
    elif p%10==1:
        print(p,'����')
    elif p%10==2 or p%10==3 or p%10==4:
        print(p,'�����')
    else:
        print(p,'������')
else:
    if p%100==11 or p%100==12 or p%100==13 or p%100==14 or p-100==11 or p-100==12 or p-100==13 or p-100==14:
         print(p,'�����')
    elif p%10==1:
        print(p,'�����')
    elif p%10==2 or p%10==3 or p%10==4:
        print(p,'�����')
    else:
        print(p,'�����')

