def diagt(m,n,i,j,s):
    s+=m[i][j]
    if(i+1==n or j+1==n):
        return s
    return diagt(m,n,i+1,j+1,s)


for _ in range(int(input())):
    n=int(input())
    m=[]
    r=[]
    for i in range(n):
        m.append(list(map(int,input().split())))
    i=0
    s=0
    for j in range(n-1,-1,-1):
        r.append(diagt(m,n,i,j,s))
    for j in range(1,n):
        r.append(diagt(m,n,j,i,s))
    print(*r)
