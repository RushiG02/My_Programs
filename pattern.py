print('-'*25,'right_angled_triangle','-'*25)

n=5
for i in range(1,n+1):
        print('*'*i)
    
print('-'*25,'right_angled_triangle1','-'*25)   
n=5
for i in range(1,n+1):
    print(' '*(n-i), end =" ") 
    print('*'*i)


print('-'*25,'triangle','-'*25)   

    
n=5
for i in range(1,n+1):
    print(' '*(n-i), end =" ") 
    print('* '*i)
    
    
    
print('-'*25,'reverse_triangle','-'*25) 

n=5
for i in range(n,0,-1):
        print(' '*(n-i),end='')
        print('* '*i)
        
        
print('-'*25,'right_angled_number_triangle1','-'*25)         
        
        
n=5
for i in range(1,n+1):
    for j in range(1,i):
        print(j,' ',end='')
    print('\n')
    
   
print('-'*25,'number_triangle1','-'*25)   
    
n=5
for i in range(1,n+1):
    print(' '*(n-i), end =" ")
    for j in range(1,i+1):
        print(j,' ',end='')
    print('\n')
    