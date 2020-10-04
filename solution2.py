import math
import ast

def FindArea(b,s):
    b.sort(key=lambda x:x[0][0])

    bh=max(b[0],key=lambda i:abs(i[-1]))
    bht=abs(bh[-1])+abs(s[-1])

    hw={}


    for i in range(len(b)):
        hw['h'+str(i)]=math.sqrt( ((b[i][0][0]-b[i][1][0])**2)+((b[i][0][1]-b[i][1][1])**2) )
        hw['w'+str(i)]=math.sqrt( ((b[i][1][0]-b[i][2][0])**2)+((b[i][1][1]-b[i][2][1])**2) )
    
    result=hw['h0']+hw['w0']
    if len(b)==1:
        return(result)
    t=hw['h0']
    for i in range(1,len(b)):
        
        if hw['h'+str(i)]<t:
            t=hw['h'+str(i-1)]
            pass
        else:

            d=math.sqrt( ((b[i-1][2][0]-b[i][1][0])**2)+((b[i-1][2][1]-b[i][1][1])**2) )
            x=d*(math.tan(math.asin((bht-hw['h0'])/(math.sqrt( ((s[0]-b[i-1][2][0])**2)+((s[1]-b[i-1][2][1])**2) )))))


            h=hw['h'+str(i)]-hw['h'+str(i-1)]+x
            

            result+=(h+hw['w'+str(i)])
            t=hw['h'+str(i)]
    return(result)


if __name__ == "__main__":

    ip=input()
    b=ast.literal_eval(ip)
    ip1=input()
    s=ast.literal_eval(ip1)

    #b=[[[4,0],[4,-5],[7,-5],[7,0]], [[0.4,-2],[0.4,-5],[2.5,-5],[2.5,-2]]]
    #s=[-3.5,1]
    #b=[[[4,0],[4,-5],[7,-5],[7,0]]]
    #s=[1,1]

    print(FindArea(b,s))
  
