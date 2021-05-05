from sys import stdin






s= stdin.readline().split()
s= ' '.join(s)

n= int(stdin.readline())
sum=0
my_l=[]
while True:
    id= s.find(' ')
    if id ==-1:
        print(s)
        break
    while s.find(' ',id+1) <= n and s.find(' ',id+1)!=-1 :
        id = s.find(' ',id+1)
    out = s[:id]
    while s[id]==' ':
        id+=1


    print(out)
    s= s[id:]