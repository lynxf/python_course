m = int(input())
stack = str(input()).split()
len_s = int(len(stack))
n = int(input())
s_dict = {}
i = 0

while i != n:
    i += 1
    fun = input().split()
    if fun[0] not in s_dict:
        s_dict[fun[0]] = {fun[1]: fun[2]}
    else:
        s_dict[fun[0]][fun[1]] = fun[2]
fin = str(input())

for j in reversed(stack):
    if fin in s_dict[j]:
        if s_dict[j][fin] == '_':
            break
        else:
            fin = s_dict[j][fin]
            len_s -= 1
    else:
        len_s -= 1
print(" ".join(stack[:len_s]))
