path='textfile1.txt'
file=open(path,'a')
file.write('Students\' information')

n=int(input('Enter No. of students: '))
for i in range(n):
    n=input('enter name: ')
    r=input('enter rollno: ')
    file.write('\n'+str(i+1) + '.'+' '+n+' '+r)

file.close()