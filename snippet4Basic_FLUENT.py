import os

#   get the current path
CWD = os.getcwd()
Case = []
Folder = []

for (root, directories, files) in os.walk(CWD):
    for file in files:
        if '.jou' in file:
            file_path = os.path.join(root, file)
            name_journal = file
            name_folder = str(root).replace(CWD, '.').split('\\')[1]
            Case.append(name_journal)
            Folder.append(name_folder)