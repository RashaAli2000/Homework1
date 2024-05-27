name=input("enter your name")
ff=open('c://qw.txt','r')
deg=0
for x in range (20):
    s=ff.readline()
    print(s)
    an=input()
    an=an+"\n"
    s=ff.readline()
    if(an==s):
        deg+=1
out=open("c:\\an.txt",'w')
out.write(name)
out.write(str(deg))
ff.close()
out.close()
