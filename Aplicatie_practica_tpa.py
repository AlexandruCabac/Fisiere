nt,ne,gr1,gr2,t,ng=0,0,[],[],0,0
with open("C:\\Users\\Phantom\\Desktop\\input.txt",'r')as f:
    data=list(f.readlines())
for i in data:
    linie=i.split()
    nt+=int(linie[2])
    if linie[3]=='Engleza'or linie[3]=='engleza':
        ne+=int(linie[2])
        gr1.append(t)
    elif linie[3]=='Germana'or linie[3]=='germana':
        ng+=int(linie[2])
        gr2.append(t)
    else:
        print("Error")
    t+=1
with open("C:\\Users\\Phantom\\Desktop\\output.txt",'w')as f:
    med=nt/t
    for i in range (len(data)):
        out=str(i+1)+':\t'+str(data[i])
        f.write(out)
    out='\n'+"Nota medie este: "+str(med)
    f.write(out)
with open("C:\\Users\\Phantom\\Desktop\\outputEngleza.txt",'w')as f:
    med=ne/(len(gr1))
    for i in range(len(gr1)):
        out=str(i+1)+':\t'+str(data[gr1[i]])
        f.write(out)
    out='\n'+"Nota medie este: "+str(med)
    f.write(out)
with open("C:\\Users\\Phantom\\Desktop\\outputGermana.txt",'w')as f:
    med=ng/(len(gr2))
    for i in range(len(gr2)):
        out=str(i+1)+':\t'+str(data[gr2[i]])
        f.write(out)
    out='\n'+"Nota medie este: "+str(med)
    f.write(out)