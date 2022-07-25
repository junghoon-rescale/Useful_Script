import os

pwd = os.getcwd()

flist=open("filelist.csv",'w')
flist.write("Case\n")

for (root, directories, files) in os.walk(pwd):
    for file in files:
        if '.xyz' in file:
            flist.write(str(file).split('.')[0] + '\n')
