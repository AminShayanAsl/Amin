import os
#--Beautiful-------------------------------
class color :
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK = '\033[95m'
    PHOSPHOR = '\033[96m'
#--Binary-----------------------------------------
def Binary(x):
    y = 0
    s,c = "",""
    if x==0:
        s = "0"
    while x>0:
        y = x % 2
        c = str(y)
        s = c + s
        x = x // 2
    return s
#--Pow--------------------------------------------
def Pow(x):
    if x==0 or x==1:
        return True
    while x>2:
        y = x % 2
        if y!=0:
            return False
        x = x // 2
    if x==2:
        return True
    return False
#--Del--------------------------------------------
def Del(a,b,L):
    for i in L:
        if i==a or i==b:
            L.remove(i)
#--Sub--------------------------------------------
def Sub(P):
    S = []
    for i in range(len(P)):
        L1 = []
        for j in range(len(P[i])):
            L0 = []
            for k in range(1,len(P[i][j])):
                x = P[i][j][k] - P[i][j][k-1]
                L0.append(x)
            L1.append(L0)
        S.append(L1)
    return S
#--Mix--------------------------------------------
def Mix(L1,L2):
    L0 = []
    for i in range(len(L1)):
        L0.append(L1[i])
        L0.append(L2[i])
    return L0
#--Exist------------------------------------------
def Exist(P,L):
    if len(P)>0:
        for I in P:
            flag = False
            for J in I:
                for k in range(len(L)):
                    if J==L[k]:
                        flag = True
                        break
                    elif J!=L[k]:
                        flag = False
            if flag==True:
                return True
        if flag==False:
            return False
    else:
        return False
#--exist------------------------------------------
def exist(L,x):
    for I in L:
        if I==x:
            return True
    return False
#--Driving program--------------------------------
n = int(input(color.PINK+"What is a multi-variable function? "))
nm = int(input(color.PINK+"Enter number of (maxterm or minterm) : "))
m,d = [],[]
for i in range(nm):
    x = int(input(color.PINK+"Enter : "))
    m.append(x)
nd = int(input(color.PINK+"Enter number of don't care : "))
for i in range(nd):
    x = int(input(color.PINK+"Enter : "))
    d.append(x)
L = []
L = m + d
B = []
for i in range(len(L)):
    a = Binary(L[i])
    B.append(a)
N1 = []
for i in B:
    x = i.count("1")
    N1.append(x)
P0 = []
for j in range(n+1):
    L0 = []
    for i in range(len(N1)):
        if N1[i]==j:
            L0.append(L[i])
    if len(L0)!=0:
        P0.append(L0)
PI = []
P1 = []
for i in range(len(P0)-1):
    L1 = []
    for j in range(len(P0[i])):
        for k in range(len(P0[i+1])):
            L0 = []
            if P0[i][j]<P0[i+1][k]:
                x = P0[i+1][k] - P0[i][j]
                flag = Pow(x)
                if flag==True:
                    Del(P0[i+1][k],P0[i][j],L)
                    L0.append(P0[i][j])
                    L0.append(P0[i+1][k])
                    L1.append(L0)
    if len(L1)!=0:
        P1.append(L1)
for i in L:
    L0 = []
    L0.append(i)
    PI.append(L0)
while True:
    T = []
    T0 = []
    P0 = []
    S = []
    S = Sub(P1)
    for i in range(len(S)-1):
        L1 = []
        for j in range(len(S[i])):
            for k in range(len(S[i+1])):
                flag = True
                for z in range(len(S[i][j])):
                    if S[i][j][z]!=S[i+1][k][z]:
                        flag = False
                        break
                    if flag==True:
                        x = P1[i+1][k][0] - P1[i][j][0]
                        f = Pow(x)
                        if f==True:
                            T0 = []
                            T0.append(i)
                            T0.append(j)
                            T.append(T0)
                            T0 = []
                            T0.append(i+1)
                            T0.append(k)
                            T.append(T0)
                            L0 = Mix(P1[i][j],P1[i+1][k])
                            f0 = Exist(L1.copy(),L0.copy())
                            if f0==False:
                                L1.append(L0)
        if len(L1)>0:
            P0.append(L1)
    for i in range(len(P1)):
        for j in range(len(P1[i])):
            f1 = False
            for t in T:
                if t[0]==i and t[1]==j:
                    f1 = True
                    break
            if f1==False:
                PI.append(P1[i][j])
    if len(P0)<2:
        if len(P0)==1:
            for j in range(len(P0[0])):
                if Exist(PI,P0[0][j])==False:
                    PI.append(P0[0][j])
        break
    P1 = P0.copy()
print(color.YELLOW+"\n-----------------------------------------\n")
for i in range(len(PI)):
    print(color.PHOSPHOR+"PI",i+1,color.RED+" :",end="")
    print(color.PINK+"",PI[i])
print(color.YELLOW+"\n-----------------------------------------\n")
print(end=color.BLUE+"\t\t")
for i in range(nm):
    print(m[i],end="\t")
print()
for i in range(len(PI)):
    s = "PI" + str(i+1) + "\t"
    for j in range(nm):
        f = exist(PI[i],m[j])
        if f==True:
            s = s + "\t*"
        else:
            s = s + "\t"
    for k in range(3):
        print(color.BLUE+s[k],end="")
    for k in range(3,len(s)):
        print(color.RED+s[k],end="")
    print()
EPI = []
L3 = m[:nm]
for i in range(len(PI)):
    for j in range(len(PI[i])):
        if exist(L3,PI[i][j]):
            flag = False
            for k in range(len(PI)):
                if k==i:
                    pass
                else:
                    flag = exist(PI[k],PI[i][j])
                    if flag==True:
                        break
            if flag==False:
                EPI.append(PI[i])
                break
print(color.YELLOW+"\n-----------------------------------------\n")
for i in range(len(EPI)):
    print(color.PHOSPHOR+"EPI",i+1,color.RED+" :",end="")
    print(color.BLUE+" ",EPI[i])
L1 = []
L2 = []
for i in range(nm):
    L0 = []
    for j in range(len(PI)):
        for k in range(len(PI[j])):
            if m[i]==PI[j][k]:
                L0.append(j+1)
    if len(L0)==1:
        L2.append(L0[0])
    elif len(L0)>1:
        L1.append(L0)
for i in range(len(L1)):
    for j in range(len(L1[i])):
        for k in L2:
            if i<len(L1):
                if len(L1[i])!=0:
                    if L1[i][j]==k:
                        if len(L1)>1:
                            L1[i] = []
                        elif len(L1)==1:
                            L1 = []
                        break
print(color.YELLOW+"\n-----------------------------------------\n")
s = ""
for I in L1:
    if len(I)!=0:
        s = s + "("
        for j in range(len(I)):
            s = s + "PI" + str(I[j])
            if j!=len(I)-1:
                s = s + " U "
        s = s + ")"
        s = s + " ^ "
L0 = []
for i in range(len(L2)):
    f = exist(L0,L2[i])
    if f==False:
        L0.append(L2[i])
        s = s + "PI" + str(L2[i])
        if i!=len(L2)-1:
            s = s + " ^ "
print(color.GREEN+"Proposition",color.RED+" = ",color.GREEN+s)