import os

pwd = os.getcwd()

flist=open("filelist.csv",'w')
flist.write("Case\n")

for (root, directories, files) in os.walk(pwd):
    for file in files:
        if '.dyn' in file:
            file_path = os.path.join(root, file)
#            print(file, ',', str(root).replace(pwd,'.'))
#            Case = str(root).replace(pwd, '.').split('\\')[1]
#            print(Case)
            flist.write(str(root).replace(pwd, '.').split('\\')[1] + '\n')
