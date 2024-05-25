import os

TARGET = r'C:\Users\halloween\Documents'
with open('backup.txt', 'w', encoding="utf-8") as f:    
    for folderName, subfolders, filenames in os.walk(TARGET):
        f.write('The current folder is ' + folderName + '\n')

        for subfolder in subfolders:
            f.write('SUBFOLDER OF ' + folderName + ': ' + subfolder + '\n')

        for filename in filenames:
            f.write('FILE INSIDE ' + folderName + ': '+ filename + '\n')

        f.write('\n\n')
