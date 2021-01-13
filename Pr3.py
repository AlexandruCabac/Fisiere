with open('globulet.txt','r') as f:
    a=f.readline()
a=str(int(a)*4+4)
with open('bradut.txt','w') as f:
    f.write(a)