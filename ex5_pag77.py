b=0
with open("C:\\Users\\Phantom\\Desktop\\test.txt",'r')as f:
    for x in f.read().split('\n'):
        for y in x:
            if y in ['A','a','E','e','I','i','O','o','U','u']:
                b+=1    
print(b)
with open("C:\\Users\\Phantom\\Desktop\\test.txt",'a')as f:
    b='\n'+str(b)
    f.write(b)