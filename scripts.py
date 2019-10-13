# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
print("Hello, World!")
# Exercise 2 - Introduction - Python If-Else
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) == 0:
        if 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
# Exercise 3 - Introduction - Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
# Exercise 4 - Introduction - Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
# Exercise 5 - Introduction - Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        if i>=0:
            print(i*i)
# Exercise 6 - Introduction - Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100  == 0:
            leap = False
            if year % 400 ==0:
                leap = True 
    return leap
year = int(input())
print(is_leap(year))
# Exercise 7 - Introduction - Print Function
if __name__ == '__main__':
    n = int(input().strip())
    print(*range(1,n+1), sep="")
# Exercise 8 - Basic data types - List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[]
    for i in range(x+1):
        for j in range(y+1):
            for p in range(z+1):
               if i+j+p!=n:
                    l.append([i,j,p])
    print(l)
# Exercise 9 - Basic data types - Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=[]
    for i in arr:
        l.append(i)
    a=min(l)
    for i in range(len(l)):
        if l[i]<max(l) and l[i]>a:
            a=l[i]

    print (a)
# Exercise 10 - Basic data types - Nested Lists
if __name__ == '__main__':
    l=[]
    l_s=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        if score not in l_s:
            l_s.append(score)
    l_s.sort()
    l.sort()
    for i in range(len(l)):
        if l_s[1]==l[i][1]:
            print(l[i][0])

# Exercise 11 - Basic data types - Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    m=0
    l=student_marks.get(query_name)
    for i in range(len(l)):
        m+=l[i]
    print(format(m/len(l),".2f"))
# Exercise 12 - Basic data types - Lists
if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        n_line=input().split()
        if n_line[0]=="print":
            print(l)
        elif n_line[0]=="append":
            l.append(int(n_line[1]))
        elif n_line[0]=="reverse":
            l.reverse()
        elif n_line[0]=="remove":
            l.remove(int(n_line[1]))
        elif n_line[0]=="pop":
            l.pop()
        elif n_line[0]=="sort":
            l.sort(key=None)
        else:
            l.insert(int(n_line[1]),int(n_line[2]))
# Exercise 13 - Basic data types - Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))
# Exercise 14 - Strings - sWAP cASE
def swap_case(s):
    z=""
    for i in range(len(s)):
        if s[i].islower()==True:
            z+=s[i].upper()
        else:
            z+=s[i].lower()
    return z
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    return string[0:position] + character + string[position+1:len(string)]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Exercise 18 - Strings - Find a string
def count_substring(string, sub_string):
    z=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string)==True:
            z+=1
    return z
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
# Exercise 19 - Strings - String Validators
if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        if s[i].isalnum()==True:
            print(True)
            break
        elif i==(len(s)-1):
            print(False)
    for i in range(len(s)):
        if s[i].isalpha()==True:
            print(True)
            break
        elif i==(len(s)-1):
            print(False)
    for i in range(len(s)):
        if s[i].isdigit()==True:
            print(True)
            break
        elif i==(len(s)-1):
            print(False)
    for i in range(len(s)):
        if s[i].islower()==True:
            print(True)
            break
        elif i==(len(s)-1):
            print(False)
    for i in range(len(s)):
        if s[i].isupper()==True:
            print(True)
            break
        elif i==(len(s)-1):
            print(False)
    

# Exercise 20 - Strings - Text Alignment 
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
# Exercise 21 - Strings - Text Wrap
import textwrap

def wrap(string, max_width):
    s=''
    for i in range(len(string)):
        s+=string[i]
        if len(s)==max_width:
            print(s)
            s=''
    return  s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
# Exercise 22 - Strings - Designer Door Mat
N=input().split()
c=int(N[0])
r=int(N[1])
for i in range(1,c//2+1):
    print("-"*(3*((c//2)-i+1))+".|."*((r-(3*((c//2)-i+1)*2))//3)+"-"*(3*((c//2)-i+1)))
print("-"*((r-7)//2)+"WELCOME"+"-"*((r-7)//2))
for i in range(1,c//2+1):
    print("-"*(3*i)+".|."*((r-((3*i)*2))//3)+"-"*(3*i))

# Exercise 23 - Strings - String Formatting
def print_formatted(number):
    w=len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# Exercise 24 - Strings - Alphabet Rangoli
def print_rangoli(size):
    import string
    a=string.ascii_lowercase
    w=4*size-3
    l=[]
    for i in range(size):
        s = "-".join(a[i:size])
        l.append((s[::-1]+s[1:]).center(w, "-"))
    print('\n'.join(l[:0:-1]+l))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
# Exercise 25 - Strings - Capitalize!

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s=s.capitalize()
    print(s)
    for i in range(len(s)-1):
        if s[i]==" ":
            s=s[0:i] + s[i:].replace(s[i+1],s[i+1].capitalize(),1)
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
# Exercise 26 - Strings - The Minion Game
def minion_game(string):
    stuart=0
    kevin=0
    vowels="AEIOU"
    for i in range(len(string)):
        if s[i] in vowels:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)

    if kevin>stuart:
        print ("Kevin", kevin)
    elif (kevin<stuart):
        print ("Stuart", stuart) ##Solution found using HACKERRANK discussions advices :(
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
# Exercise 27 - Strings - Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    l=[]
    count=0
    for i in range(len(string)):
        if string[i] not in l:
            l.append(string[i])
        count+=1
        if count==k:
            count=0
            print ("".join(l))
            l=[]
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# Exercise 28 - Sets - Introduction to Sets
def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# Exercise 29 - Sets - No Idea!
integ=input().split()
n=input().split()
A=set(input().split())
B=set(input().split())
happy=0
for i in range(len(n)):
    if n[i] in A:
        happy+=1
    if n[i] in B:
        happy-=1
print(happy)
# Exercise 30 - Sets - Symmetric Difference
m=int(input())
set1=set(map(int,input().split()))
m2=int(input())
set2=set(map(int,input().split()))
set3=set1.difference(set2).union(set2.difference(set1))
for i in range(len(set3)):
    print(min(set3))
    set3.remove(min(set3))
# Exercise 31 - Sets - Set .add()
n=int(input())
mys=set()
for i in range(n):
    a=input()
    mys.add(a)
print(len(mys))
# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))
m=int(input())
for i in range(m):
    st=input().split()
    if st[0]=="pop":
        s.pop()
    elif st[0]=="remove":
        s.remove(int(st[1]))
    elif st[0]=="discard":
        s.discard(int(st[1]))
print(sum(s))
# Exercise 33 - Sets - Set .union() Operation
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
print(len(s1.union(s2)))
# Exercise 34 - Sets - Set .intersection() Operation
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
print(len(s1.intersection(s2)))
# Exercise 35 - Sets - Set .difference() Operation
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
print(len(s1.difference(s2)))
# Exercise 36 - Sets - Set .symmetric_difference() Operation
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))
print(len(s1.symmetric_difference(s2)))
# Exercise 37 - Sets - Set Mutations
n=int(input())
s1=set(map(int,input().split()))
m=int(input())
for i in range(m):
    s=input().split()
    if s[0]=="intersection_update":
        s1.intersection_update(set(map(int,input().split())))
    elif s[0]=="update":
        s1.update(set(map(int,input().split())))
    elif s[0]=="symmetric_difference_update":
        s1.symmetric_difference_update(set(map(int,input().split())))
    else:
        s1.difference_update(set(map(int,input().split())))
print(sum(s1))
# Exercise 38 - Sets - The Captain's Room
n=int(input())
l=list(map(int,input().split()))
s=set(l)
l.sort()
i=0
while i<(len(l)-1):
    if l[i]==l[i+1]:
        s.discard(l[i])
        i+=n
print(sum(s))
# Exercise 39 - Sets - Check Subset
n_t=int(input())
for i in range(n_t):
    elA=int(input())
    A=set(map(int,input().split()))
    elB=int(input())
    B=set(map(int,input().split()))
    if len(A.union(B))==len(B):
        print(True)
    else:
        print(False)
# Exercise 40 - Sets - Check Strict Superset
A=set(map(int,input().split()))
n=int(input())
y=0
for i in range(n):
    B=set(map(int,input().split()))
    if A.issuperset(B)==True:
        y+=1
if y==n:
    print(True)
else:
    print(False)
# Exercise 41 - Collections - collections.Counter()
from collections import Counter
n=int(input())
l=list(map(int,input().split())) #1st version without using counter
m=int(input())
money=0
c=Counter(l)
for i in range(m):
    s=list(map(int,input().split()))
    if c[s[0]]>0:
        c[s[0]]=c[s[0]]-1
        money+=s[1]
print(money)
##########################################
from collections import Counter
n=int(input())
l=list(map(int,input().split()))
m=int(input())
money=0
for i in range(m):
    s=list(map(int,input().split()))
    if s[0] in l:
        money+=s[1]
        l.remove(s[0])
print(money)
# Exercise 42 - Collections - DefaultDict Tutorial
from collections import defaultdict
n=list(map(int,input().split()))
d=defaultdict(list)
for i in range(n[0]):
    d["A"].append(input())
for i in range(n[1]):
    d["B"].append(input())
for i in d.get("B"):
    s=''
    for j in range(len(d.get("A"))):
        if d.get("A")[j]==i:
            s+=str(j+1)+" "
    if s!="":
        print(s)
    else:
        print("-1")
# Exercise 43 - Collections - Collections.namedtuple()
from collections import namedtuple
n=int(input())
Student=namedtuple("Student",input().split())
markstot=0
for i in range(n):
    a,b,c,d=input().split()
    student=Student(a,b,c,d)
    markstot+=int(student.MARKS)
print("{0:.2f}".format(markstot/n))

# Exercise 44 - Collections - Collections.OrderedDict()
from collections import OrderedDict
d=OrderedDict()
n=int(input())
l=set()
for i in range(n):
    p=''
    s=list(input().split())
    qnt=int(s[len(s)-1])
    s.remove(s[len(s)-1])
    for j in range(len(s)):
        if j==len(s)-1:
            p+=s[j]
        else:
            p+=s[j]+" "
    l.add(p)
    if p in d:
        d[p]=d[p]+qnt
    else:
        d[p]=qnt
for k,v in d.items():
    print(k,v)
# Exercise 45 - Collections - Word Order
from collections import OrderedDict
n=int(input())
d=OrderedDict()
for j in range(n):
    p=input()
    if p in d:
        d[p]+=1
    else:
        d[p]=1
print(len(d))
print(*d.values())
# Exercise 46 - Collections - Collections.deque()
from collections import deque
d=deque()
n=int(input())
for i in range(n):
    s=input().split()
    if s[0]=="append":
        d.append((s[1]))
    elif s[0]=="pop":
        d.pop()
    elif s[0]=="popleft":
        d.popleft()
    else:
        d.appendleft((s[1]))
print(" ".join(d))
# Exercise 47 - Collections - Company Logo
from collections import Counter

if __name__ == '__main__':
    s = input()
    p=[]
    c=Counter()
    for z in range(len(s)):
        p.append(s[z])
    p.sort()
    for i in range(len(p)):
        c[p[i]]+=1
    l=list(c.most_common(3))
    for j in range(len(l)):
        print(l[j][0],str(l[j][1]))
# Exercise 48 - Collections - Piling Up!
from collections import deque
n = int(input())
for i in range(n):
    t=input() #uselss
    c=deque(input().strip().split())
    s=""
    for j in range(len(c)):
        left=c[0]
        right =c[len(c)-1]
        if left>=right:
            if s>=left or s=="":
                 s=left
                c.popleft() ##I've done just a part of the exercise, I get some help from the discussion section, for example I was trying to do the exercise using just lists
        else:
            if s>=right or s=="":
                s=right
                c.pop()
    if len(c)==0:
        print('Yes')
    else:
        print('No')

# Exercise 49 - Date time - Calendar Module
import calendar
n=list(map(int,input().split()))
l=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print (l[calendar.weekday(n[2], n[0], n[1])])
# Exercise 50 - Date time - Time Delta
from datetime import datetime
def time_delta(t1, t2):
    s1=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    s2=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((s1-s2).total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
# Exercise 51 - Exceptions -
n=int(input())
for i in range(n):
    l1=input().split()
    try:
        print(int(l1[0])//int(l1[1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as w:
        print("Error Code:", w)
# Exercise 52 - Built-ins - Zipped!
n=input().split()
z=list(zip(*(list(map(float,input().split())) for _ in range(int(n[1])))))
for i in range(int(n[0])):
    print("{:.2f}".format(sum(z[i])/float(n[1])))
# Exercise 53 - Built-ins - Athlete Sort
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    l2=[]
    for i in range(n):
            l2.append(arr[i][k])
    l2=list(set(l2))
    l2.sort()
    for j in range(len(l2)):
        for z in range(n):
            if l2[j]==arr[z][k]:
                print(" ".join(map(str,arr[z])))
# Exercise 54 - Built-ins - Ginorts
s=input()
l=[]
ns=""
for i in range(len(s)):
    l.append(s[i])
l.sort()
for j in range(len(l)):
    if l[j].islower()==True:
        ns=ns + l[j]
for i in range(len(l)):
    if l[i].isupper()==True:
        ns+=l[i]
for i in range(len(l)):
    if l[i].isdigit()==True and int(l[i])%2!=0:
        ns+=l[i]
for i in range(len(l)):
    if l[i].isdigit()==True and int(l[i])%2==0:
        ns+=l[i]
print(ns)
# Exercise 55 - Map and lambda function
cube = lambda l: pow(l,3) # complete the lambda function 
def fibonacci(n):
    l=[]
    i=0
    j=1
    while len(l)<n:
        l.append(i)
        i,j = j,i+j
    return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
# Exercise 56 - Regex - Detect Floating Point Number
import re
n=int(input())
for i in range(n):
    s=input()
    x=re.match(r'^[-+]?[0-9]*\.[0-9]+$',s)
    print (bool(x))
# Exercise 57 - Regex - Re.split()
regex_pattern = r"[.,]+"	# Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))
# Exercise 58 - Regex - Group(), Groups() & Groupdict()
import re
w=input().strip()
q=(re.search(r"([a-zA-Z0-9])\1+", w))
if q==None:
    print("-1")
else:
    print(q.group(1))
#(re.match("[^w]", w))
# Exercise 59 - Regex - Re.findall() & Re.finditer()
import re
s=re.findall(r'(?=[^AEIOUaeiou]?)([AEIOUaeiou]{2,})(?=[^AEIOUaeiou])+',input())
if len(s)==0:
    print("-1")
else:
    print("\n".join(s))
# Exercise 60 - Regex - Re.start() & Re.end()
import re
s=input()
k=input()
m=re.compile(k)
a=m.search(s)
if a==None:
    print("(-1, -1)")
#for i in range(len(s)):
#    print((a.start(),a.end()-1))
#    a=m.search(s,a.start()+1)    it's giving me Runtime Error and idk how to let it be faster than this so I have to look for a way to do it
while a:
    print((a.start(),a.end()-1))
    a=m.search(s,a.start()+1)
# Exercise 61 - Regex - Regex Substitution
import re
n=int(input())
for i in range(n):
    s=input()    
    s=re.sub(r" \&\&(?= )", " and", s) #Pretty hard
    s=re.sub(r" \|\|(?= )", " or", s) #Get helped from the discussion section
    print(s)
# Exercise 62 - Regex - Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM){0,3}D?(CD){0,3}C{0,3}(XC){0,3}L?(XL){0,3}X{0,3}(IX){0,3}V?(IV){0,3}I{0,3}$|^m{0,3}(cm){0,3}d?(cd){0,3}c{0,3}(xc){0,3}l?(xl){0,3}x{0,3}(ix){0,3}v?(iv){0,3}i{0,3}$"	# Do not delete 'r'.
##Got some help in the discussion section
import re
print(str(bool(re.match(regex_pattern, input()))))
# Exercise 63 - Regex - Validating phone numbers
import re
n=int(input())
for i in range(n):
    s=input()
    a=re.match(r"^[7-9]\d{9}$",s)
    if a==None:
        print("NO")
    else:
        print("YES")
# Exercise 64 - Regex - Validating and Parsing Email Addresses
#import email.utils
import re
n=int(input())
for i in range(n):
    s=input().split()
    r=re.match(r"^(<([A-Za-z]+[0-9-._a-zA-Z]*)@[a-z]+\.([a-z]{1,3})>)$", s[1])
    if r==None:
        continue
    else:
        print(" ".join(s))
# Exercise 65 - Regex - Hex Color Code
import re
n=int(input())
l=[]
for i in range(0,n):
    try:
        s=input()
    except EOFError:
        continue
    a=s.split()
    if len(a)>1 and  '{' not in a:
        z=re.findall(r'#[0-9a-fA-F]{3,6}',s)
        if len(z)>0:
            for j in z:
                l.append(j)
print("\n".join(l))
# Exercise 66 - Regex - HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def _attr_printer(self, attrs):
        if attrs:
            for attr in attrs:
                print("-> " + attr[0] + " > " + str(attr[1]) )
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self._attr_printer(attrs)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self._attr_printer(attrs) 
n = int(input())
h=""
for i in range(n):
    s=input()
    h+=s
p=MyHTMLParser()
p.feed(h)
# Exercise 67 - Regex - HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if len(data.split('\n')) == 1:
            print('>>> Single-line Comment')
            print(data)
        else:
            print('>>> Multi-line Comment')
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
# Exercise 68 - Regex - Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        for j in attr:
            print("->", j[0], ">", j[1])
parser = MyHTMLParser()
n=int(input())
for i in range(n):
    s=input()
    parser.feed(s)
# Exercise 69 - Regex - Validating UID
import re
rem = r"(?!.*(.).*\1)"
up = r"(?=(?:.*[A-Z]){2,})"
di = r"(?=(?:.*\d){3,})"
nu = r"[a-zA-Z0-9]{10}"
n=int(input())
for i in range(n):
    s=input()
    if re.match(rem, s)!=None and re.match(up, s)!=None and re.match(di, s)!=None and re.match(nu, s)!=None:
        print("Valid")
    else:
        print("Invalid")
# Exercise 70 - Regex - Validating Credit Card Numbers
import re
n=int(input())
for i in range(n):
    s=input()
    if re.search(r"([\d])\1\1\1",s.replace("-", ""))!=None:
        print("Invalid")
    else:
        if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s):
            print("Valid")
        else:
            print("Invalid")
# Exercise 71 - Regex - Validating Postal Codes
# Exercise 72 - Regex - Matrix Script
# Exercise 73 - Xml - XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    # your code goes here
    return etree.tostring(node).count(b'=') #You have a value after a "=", so you have just to count how many of them are in the XML file
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
# Exercise 74 - Xml - XML 2 - Find the Maximum Depth
# Exercise 75 - Closures and decorators - Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        l1=[]
        s=""
        for i in range(len(l)):
            if l[i][0]=="0":
                s="+91"+" "+l[i][1:6]+" "+l[i][6:len(l[i])]
                l1.append(s)
            elif len(l[i])==13:
                s=l[i][0:3]+" "+l[i][3:8]+" "+l[i][8:len(l[i])]
                l1.append(s)
            elif len(l[i])==10:
                s="+91"+" "+l[i][0:5]+" "+l[i][5:len(l[i])]
                l1.append(s)
            elif len(l[i])==12:
                s="+"+l[i][0:2]+" "+l[i][2:7]+" "+l[i][7:len(l[i])]
                l1.append(s)
        l1.sort()
        print("\n".join(l1))
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
# Exercise 76 - Closures and decorators - Decorators 2 - Name Directory
import operator
def person_lister(f):
    def inner(people):
        s=sorted(people, key=lambda x: int(x[2]))  #I got the int() advice on the discussion section
        return map(f,s)
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
# Exercise 77 - Numpy - Arrays
import numpy
def arrays(arr):
    a = numpy.array(arr,float)[::-1]
    return a
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
# Exercise 78 - Numpy - Shape and Reshape
import numpy
print (numpy.reshape(numpy.array(list(map(int,input().split()))),(3,3)))
# Exercise 79 - Numpy - Transpose and Flatten
import numpy
nxm=list(map(int,input().split()))
l=[]
for i in range(nxm[0]):
    s=list(map(int,input().strip().split()))
    l.append(s)
a=numpy.array(l)
print(numpy.transpose(a))
print (a.flatten())
# Exercise 80 - Numpy - Concatenate
import numpy
nxm=list(map(int,input().split()))
a=numpy.array([input().split() for _ in range(nxm[0])],int)
b=numpy.array([input().split() for _ in range(nxm[1])],int)
print(numpy.concatenate((a,b), axis = 0))
# Exercise 81 - Numpy - Zeros and Ones
import numpy
n=list(map(int,input().split()))
for i in range(n[1]):
    a=numpy.array(numpy.zeros(n),int)
print(a)
for i in range(n[1]):
    a=numpy.array(numpy.ones(n),int)
print(a)
# Exercise 82 - Numpy - Eye and Identity
import numpy
n=list(map(int,input().split()))
a=numpy.eye(n[0], n[1], k = 0)
numpy.set_printoptions(sign=' ') #got helped from the discussion section for this command that I didn't know
print(a)
# Exercise 83 - Numpy - Array Mathematics
import numpy
nxm=list(map(int, input().split()))
a=numpy.array([input().split() for _ in range(nxm[0])],int)
b=numpy.array([input().split() for _ in range(nxm[0])],int)
print (numpy.add(a, b))
print (numpy.subtract(a, b))
print (numpy.multiply(a, b))
print (a//b)
print (numpy.mod(a, b))
print (numpy.power(a, b))
# Exercise 84 - Numpy - Floor, Ceil and Rint
import numpy
a=numpy.array(list(map(float, input().split())))
numpy.set_printoptions(sign=' ') 
print (numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
# Exercise 85 - Numpy - Sum and Prod
import numpy
nxm=list(map(int, input().split()))
a=numpy.array([input().split() for _ in range(nxm[0])],int)
print (numpy.prod(numpy.sum(a, axis = 0)))
# Exercise 86 - Numpy - Min and Max
import numpy
nxm=list(map(int, input().split()))
a=numpy.array([input().split() for _ in range(nxm[0])],int)
print(numpy.max(numpy.min(a, axis=1)))
# Exercise 87 - Numpy - Mean, Var, and Std
import numpy
nxm=list(map(int, input().split()))
a=numpy.array([input().split() for _ in range(nxm[0])],int)
numpy.set_printoptions(sign=" ")
numpy.set_printoptions(legacy='1.13') #I didn't know about this storytelling of the legacy of the version of numpy, I found this things after many running
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(numpy.std(a, axis=None))
# Exercise 88 - Numpy - Dot and Cross
import numpy
nxm=int(input())
a=numpy.array([input().split() for _ in range(nxm)],int)
b=numpy.array([input().split() for _ in range(nxm)],int)
print((numpy.dot(a,b)))
# Exercise 89 - Numpy - Inner and Outer
import numpy
a=numpy.array(list(map(int,input().split())))
b=numpy.array(list(map(int,input().split())))
print(numpy.inner(a,b))
print(numpy.outer(a,b))
# Exercise 90 - Numpy - Polynomials
import numpy
a=numpy.array(list(map(float,input().split())))
print(numpy.polyval(a,int(input())))
# Exercise 91 - Numpy - Linear Algebra
import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)], float)
numpy.set_printoptions(legacy="1.13") #again test failed because of this
print (numpy.linalg.det(a))

# ===== PROBLEM2 =====

# Exercise 92 - Challenges - Birthday Cake Candles
def birthdayCakeCandles(ar):
    c=ar.count(max(ar))
    return c
# Exercise 93 - Challenges - Kangaroo
def kangaroo(x1, v1, x2, v2):
    if v2>=v1:
        return "NO"
    elif (x1-x2)%(v2-v1)==0: #math problem
        return "YES"
    else:
        return "NO"
# Exercise 94 - Challenges - Viral Advertising
def viralAdvertising(n):
    c=0
    p=5
    l=0
    for i in range(n):
        l=p//2
        p=l*3
        c+=l
    return c
# Exercise 95 - Challenges - Recursive Digit Sum
def superDigit(n):
    c=0
    if len(n)==1:
        return n
    for i in range(len(n)):
        c+=int(n[i])
    return superDigit(str(c))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k=int(str(nk[1][0])) #Dat move
    result = superDigit(n*k)

    fptr.write(str(result) + '\n')

    fptr.close()

# Exercise 96 - Challenges - Insertion Sort - Part 1
# Exercise 97 - Challenges - Insertion Sort - Part 2
