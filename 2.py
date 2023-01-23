f = open('mat_dv.txt', 'r')

cls = []
res = []

for i in f:
    child = i.split()
    if cls.count(child[2]) == 0:
        cls.append(child[2])

for i in cls:
    max_all = 0
    for j in f:
        ch = j.split()
        cl = ch[2]
        if cl == i:
            summa = int(ch[3]) + int(ch[4])
            if summa > max_all:
                max_all = summa

    res.append(str(i)+' '+str(max_all))

print(cls)
print (res)
