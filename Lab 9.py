#1
'''n=list(map(int,input().split()))
even=[]
odd=[]
for i in n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)'''
#2
'''s=input()
w=s.split()
words=[]
for i in w:
    if len(i)>3:
        words.append(i)
print(words)'''
#3
'''ball=input().split()
total=0
W=0
B=0
over=[]
run=0
for i in range(len(ball)):
    a=ball[i]
    if a=='W':
        W+=1
    else:
        r=int(a)
        total+=r
        run+=r
        if r==4 or r==6:
            B+=1
    if (i+1)%6==0:
        over.append(run)
        run=0
if len(ball)%6!=0:
    over.append(run)
print('total runs:',total)
print('wicket:',W)
print('boundaries:',B)
print('runs per over:',over)'''
#4
'''n=list(map(int,input().split))
l=n[0]
s=n[0]
for i in n:
    if i>l:
        l=i
    if i<s:
        s=i
print('largest:',l)
print('smallest:',s)'''
#5
'''s=input()
w=s.split()
l=w[0]
for i in w:
    if len(i)>len(l):
        l=i
print(l)'''
#6
'''menu=input().split()
p=list(map(int,input().split()))
order=input().split()
total=0
for i in range(len(menu)):
    a=menu[i]
    quantity=order.count(a)
    if quantity>0:
        total+=quantity*p[i]
        print(a,"X",quantity,"=",quantity*p[i])
print('Total:',total)'''
#7
'''s=input()
word=s.split()
result=[]
for i in word:
    result.append(i[::-1])
print(" ".join(result))'''
#8
'''s=input()
digit=[]
sum=0
for i in s:
    if i.isdigit():
        digit.append(int(i))
        sum+=int(i)
print(digit)
print("Sum:",sum)'''
#9
'''n=int(input())
count={}
for i in range(n):
    a=input().split()
    first=a[0].lower()
    last=a[1].lower()
    name=first+"."+last
    if name not in count:
        count[name]=i
        email=name+"@jklu.edu.in"
    else:
        count[name]+=1
        email=name+str(count[name])+"@jklu.edu.in"
        
    print(email)'''
#10
'''n=list(map(int,input().split()))
result=[]
zeros=0
for i in n:
    if i==0:
        zeros+=1
    else:
        result.append(i)
for i in range(zeros):
    result.append(0)
print(result)'''














