import os
import shutil
"""
para saber el path
"""
cwd = os.getcwd() 
print("Current working directory:", cwd)


"""
para crear un archivo

f = "my_life.txt"
open("/Users/dandrade/Documents/Python course/Chatbot/"+f, 'x') #para crear un archivo
"""

"""
listar archivos en un path/directory

cwd = os.getcwd()
path = cwd
dir_list = os.listdir(path)
print("Files and directories in '",path, "' :") 
print(dir_list)
"""

"""
Eliminar archivos de un path/directory

file = "test.txt"
location = "/Users/dandrade/Documents/Python course/Chatbot/Modules/"
path = os.path.join(location, file) 
os.remove(path)
"""


"""
#Encontrar un archivo

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


filepath = findfile("my_life.txt", "/")
print(f" this is the filepath:{filepath}")

#para encnontrar ejectubales con shutil
cmd = "my_life.txt"
locate = shutil.which(cmd)
print(f" this is the filepath with shutil:{locate}")
"""

"""
Mover archivos usando shutil + os


file_source = "/Users/dandrade/Documents/Python course/Chatbot/Modules/"
file_destination = "/Users/dandrade/Documents/Python course/Chatbot/"
name = "my_life.txt"
get_files = os.listdir(file_source)

for g in get_files:
    if name in g:
        shutil.move(file_source + name, file_destination)
    else:
        print("Archivo no encontrado")
"""

"""
Para renombrar archivos

file_oldname = os.path.join("/Users/dandrade/Documents/Python course/Chatbot/", "my_lyfe.txt")
file_newname_newfile = os.path.join("/Users/dandrade/Documents/Python course/Chatbot/", "my_life.txt")

os.rename(file_oldname, file_newname_newfile)
"""

"""
Para cambiar permisos

perm = os.stat("/Users/dandrade/Documents/Python course/Chatbot/my_life.txt")
print(perm.st_mode)

os.chmod("/Users/dandrade/Documents/Python course/Chatbot/my_life.txt", 0o755)
print(perm.st_mode)
"""

"""

Crear un directorio



directory = "Test"
parent_dir = "/Users/dandrade/Documents/Python course/Chatbot/"
path = os.path.join(parent_dir, directory)
 
os.mkdir(path)
print("Directory '% s' created" % directory)
"""

