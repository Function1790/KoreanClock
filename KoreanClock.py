import os
import time as t
import datetime as d

h=["영","한","두","세","네","다섯","여섯","일곱","여덟","아홉","열"]
m=["","일","이","삼","사","오","육","칠","팔","구","십"]

def getN(n,j):
    global m
    if n==0:
        return m[n]
    elif n//10==0:
        return m[n]+" "+j
    elif n//10==1:
        return m[10]+m[n%10]+" "+j
    else:
        return m[n//10]+m[10]+m[n%10]+" "+j

def toKorean(hour, min, sec):
    global h,m
    dy="오전"
    if hour>12:
        dy="오후"
        hour-=12

    if hour//10==0:
        a=h[hour]
    else:
        a=h[10]+h[hour%10]
        if hour%10==0:
            a=h[10]

    b=getN(min,"분")
    c=getN(sec,"초")

    result=dy+"\t"+a+" 시\t"+b+"\t"+c
    return result

def StopWatch():
    a=0
    b=0
    while True:
        if b>=60:
            a+=1
            b=0
        if a>24:
            a=0
            b=0
            break
        print(toKorean(a,b,0))
        t.sleep(1)
        os.system("cls")
        b+=1

def StartTime():
    time=""
    while True:
        now=t.localtime()
        if time!=toKorean(now.tm_hour,now.tm_min,now.tm_sec):
            os.system("cls")
            time=toKorean(now.tm_hour,now.tm_min,now.tm_sec)
            print(time)
        t.sleep(0.1)
            

StartTime()