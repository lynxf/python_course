def p(file):
    f = open(file, "r")
    f = f.strip()
    t = f.split('.')
    k = open("3.txt", "w")
    for i in t:
        i = i.split()
        l = []
        if word in i:
            if "yo"==(word[-2]+word[-1]):
              l.append((word+" "))
            k.write(l+"\n")
    k.close()
    
    была еще попытка

def p(file):
    f = open(file, "r")
    k = []
    for i in f:
        k.append(i)
    print(k)
    #f = ' '.join(f.split())
    d = open("3.txt", "w")
    for i in k:
        i = i.split()
        l = []
        if j in i:
            if "yo"==(j[-2]+j[-1]):
              l.append((j+" "))
            d.write(l+"\n")
    d.close()
p("1.txt")

а потом я посидела еще немного)

def p(file):
    file = open(file, "r")
    f = file.read()
    file.close()
    file_work = [i for i in f.replace("\n", " ").split(".")]
    for i in range(len(file_work)):
        file_work[i] = file_work[i].split()
    d = open("3.txt", "w")
    for i in file_work:
        l = []
        for j in i:
            if "yo"==(j[-2]+j[-1]):
                d.write(j+" ")
        d.write("\n")
    d.close()
