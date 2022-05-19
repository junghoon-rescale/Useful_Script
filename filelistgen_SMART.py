import os

pwd = os.getcwd()

flist=open("filelist.csv",'w')
flist.write("name, folder\n")


for (root, directories, files) in os.walk(pwd):
    for file in files:
        if '.inp' in file:
            file_path = os.path.join(root, file)
            #print(file, ',', str(root).replace(pwd,'.'))
            flist.write(file+','+str(root).replace(pwd,'.')+'\n')


