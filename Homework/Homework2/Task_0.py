def plural(n, staff ) :
    n %= 100
    n1 = n % 10
    if 10 < n < 20:
        return staff[2]
    elif 1 < n1 < 5:
        return staff[1]
    elif n1 == 1:
        return staff[0]
    else :
        return staff[2]
iron = ['����','�����','������']
spoon = ['�����','�����','�����']
harmonica = ['��������','��������','��������']
kettle = ['������','�������','��������']
word = input ()
count = int(input())
if word == '����':
    proper_word = plural(count, iron)
elif word == '��������':
    proper_word = plural(count, harmonica)
elif word == '������':
    proper_word = plural(count, kettle)
else:
    proper_word = plural(count, spoon)
print(count, proper_word)
