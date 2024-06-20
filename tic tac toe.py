import os
import random
a=["1","2","3","4","5","6","7","8","9"]
print(a[0], "|", a[1], "|", a[2])
print(a[3], "|", a[4], "|", a[5])
print(a[6], "|", a[7], "|", a[8])
print("----------")
l=random.choice([1,0])
k=0
q=1
t=[0,0,0,0,0,0,0,0,0,0]
while q<=9 and q>=1:
    i="false"
    if q%2==l:
        s = int(input("enter a number for *"))
        if s>9 or s<1:
            print("invalid number")
            continue
        for f in range(1, 10):
            if t[f] == s:
                print("used number")
                i="true"
        if i=="true":
            continue
        if str(s)==a[0]:
            a[0]="*"
        elif str(s)==a[1]:
            a[1]="*"
        elif str(s)==a[2]:
            a[2]="*"
        elif str(s)==a[3]:
            a[3]="*"
        elif str(s)==a[4]:
            a[4]="*"
        elif str(s)==a[5]:
            a[5]="*"
        elif str(s)==a[6]:
            a[6]="*"
        elif str(s)==a[7]:
            a[7]="*"
        elif str(s)==a[8]:
            a[8]="*"
    else:
        s = int(random.choice([1,2,3,4,5,6,7,8,9]))
        for f in range(1, 10):
            if t[f] == s:
                i="true"
        if i=="true":
            continue
        if str(s) == a[0]:
            a[0] = "0"
        elif str(s) == a[1]:
            a[1] = "0"
        elif str(s) == a[2]:
            a[2] = "0"
        elif str(s) == a[3]:
            a[3] = "0"
        elif str(s) == a[4]:
            a[4] = "0"
        elif str(s) == a[5]:
            a[5] = "0"
        elif str(s) == a[6]:
            a[6] = "0"
        elif str(s) == a[7]:
            a[7] = "0"
        elif str(s) == a[8]:
            a[8] = "0"

    print(a[0], "|", a[1], "|", a[2])
    print(a[3], "|", a[4], "|", a[5])
    print(a[6], "|", a[7], "|", a[8])
    if q!=9:
        print("----------")
    if (a[0] == "0" and a[1] == "0" and a[2] == "0") or (a[0] == "0" and a[4] == "0" and a[8] == "0") or (
            a[0] == "0" and a[3] == "0" and a[6] == "0") or (a[2] == "0" and a[5] == "0" and a[8] == "0") or (
            a[8] == "0" and a[7] == "0" and a[6] == "0") or (a[1] == "0" and a[4] == "0" and a[7] == "0") or (
            a[3] == "0" and a[4] == "0" and a[5] == "0") or (a[2] == "0" and a[4] == "0" and a[6] == "0"):
        print("you lost")
        k=1
        break
    elif (a[0] == "*" and a[1] == "*" and a[2] == "*") or (a[0] == "*" and a[4] == "*" and a[8] == "*") or (
            a[0] == "*" and a[3] == "*" and a[6] == "*") or (a[2] == "*" and a[5] == "*" and a[8] == "*") or (
            a[8] == "*" and a[7] == "*" and a[6] == "*") or (a[1] == "*" and a[4] == "*" and a[7] == "*") or (
            a[3] == "*" and a[4] == "*" and a[5] == "*") or (a[2] == "*" and a[4] == "*" and a[6] == "*"):
        print("you won")
        k = 1
        break
    t[q] = s
    q+=1
if k==0:
    print("draw")
y=input("press \"enter\" key")

