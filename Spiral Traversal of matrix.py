q=int(input())
for _ in range(q):
    r=[]
    f=[]
    s=[]
    n=list(map(int,input().split()))
    for i in range(n[0]):
        f.append(list(map(int,input().split())))
    n1=list(map(int,input().split()))
    for i in range(n1[0]):
        s.append(list(map(int,input().split())))
    for i in range(n[0]):
        l=[]
        for j in range(n1[1]):
            p=0
            for k in range(n1[0]):
                p+=f[i][k]*s[k][j]
            l.append(p)
        r.append(l)
    for i in range(n[0]):
        print(*r[i])
