import os
all_files=[]
for root,dinr,file in os.walk(r"C:\Users\Rushi\Desktop\Deep_Learning_A_Z"):
    for fn in file:
        f=os.path.join(root,fn)
        a=os.path.abspath(f)
        all_files.append(a)

print(all_files)
input()
