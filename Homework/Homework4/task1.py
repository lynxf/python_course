
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
            if "yo" == (j[-2]+j[-1]):
                d.write(j+" ")
        d.write("\n")
    d.close()
