a=str(input())
p=int(input())
if a=='утюг':
    if p%100==11 or p%100==12 or p%100==13 or p%100==14 or p-100==11 or p-100==12 or p-100==13 or p-100==14:
         print(p,'утюгов')
    elif p%10==1:
        print(p,'утюг')
    elif p%10==2 or p%10==3 or p%10==4:
        print(p,'утюга')
    else:
        print(p,'утюгов')
else:
    if p%100==11 or p%100==12 or p%100==13 or p%100==14 or p-100==11 or p-100==12 or p-100==13 or p-100==14:
         print(p,'ложек')
    elif p%10==1:
        print(p,'ложка')
    elif p%10==2 or p%10==3 or p%10==4:
        print(p,'ложки')
    else:
        print(p,'ложек')

