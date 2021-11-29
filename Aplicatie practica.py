e,n,s=[],0,''
with open("c:\\Users\\STATIE-6-C100\\Desktop\\input.txt",'r') as f:
    while True:
        a=f.readline()
        if len(a)==0:
            break
        else:
            if '\n' in a:
                a=a[:-1]
            e.append(a.split(' '))
for i in range(len(e)):
    x=e[i]
    n+=int(x[-1])
n=n/len(e)
with open("c:\\Users\\STATIE-6-C100\\Desktop\\output.txt",'w') as f:
    for x in e[0]:
        s1=str(x)
        s=s+s1+' '
    f.write(s[:-1])
    for i in range(1,len(e)):
        s=''
        for x in e[i]:
            s1=str(x)
            s=s+s1+' '
        s1='\n'+s[:-1]
        f.write(s1)
    s1='\n'+"Nota medie"+str(n)
    f.write(s1)