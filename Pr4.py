with open('input.txt','r') as f:
    a=f.read()
a=str(int(a)-2)+' '+str(int(a)-1)+' '+str(int(a))+' '+str(int(a)+1)+' '+str(int(a)+2)+' '
with open('output.txt','w') as f:
    f.write(a)