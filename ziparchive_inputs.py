import os
import zipfile

CWD = os.getcwd()
Folder_Inputs = CWD + '\\' + 'Input Files'
# The folder name "Input Files" should be changed as yours
os.chdir(Folder_Inputs)


List_inputfiles = []

for (root, directories, files) in os.walk(Folder_Inputs):
    for file in files:
        List_inputfiles.append(file)

print(List_inputfiles)

with zipfile.ZipFile("inputfiles.zip", "w") as zip_inputs:
    for file in List_inputfiles:
        zip_inputs.write(file)
    zip_inputs.close()
