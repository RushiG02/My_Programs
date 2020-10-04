import math
import ast
def CalcArea(a):
    b=a.copy()
    b.append(a[0])
    t=0
    for i in range(len(b)-1):
        j=i+1
        t+=((b[i][0]*b[j][1])-(b[i][1]*b[j][0]))

    return(abs(t)/2)
def ReplaceNear(p,a):
    d=math.sqrt( ((p[0]-a[0][0])**2)+((p[1]-a[0][1])**2) )
    idx=0
    
    for i in a:
        d1=math.sqrt( ((p[0]-i[0])**2)+((p[1]-i[1])**2) )
        if d1<=d:
            d=d1
            idx=a.index(i)
    a[idx]=p
    return(a)
def IsPin(a,p):
    area1=CalcArea(a)
    ReplaceNear(p,a)
    area2=CalcArea(a)
    if area1>area2:
        return('True')
    else:
        return('False')

if __name__ == "__main__":

    ip=input()
    a=ast.literal_eval(ip)
    ip1=input()
    p=ast.literal_eval(ip1)
    print(IsPin(a,p))
  
    


