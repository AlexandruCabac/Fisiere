with open('numar.txt','r') as f:
    a=f.read()
with open('inmultire.txt','w') as f:
    for i in range(1,11):
        f.write(str(i)+'x'+a+'='+str(i*int(a))+'\n')