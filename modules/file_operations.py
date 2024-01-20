import csv
import os
import shutil
import stat #proporciona constantes/funciones para interpretar los resultados de os.stat() y os.lstat(). Esta “estadística” proporciona los indicadores de permiso 
            #que necesitaremos para cambiar los permisos de archivo en el usuario, grupo u otros usuarios.

class file:
    def __init__(self, name_archivo, path):
        self.name = name_archivo
        self.path = path

    def __str__(self):
        return f"El nombre del archivo que ud va a abrir es : {self.name}" 

    def crear_archivo(self):
        open("/Users/dandrade/Documents/Python course/Chatbot/"+self.name, 'x')
        print(f"Has creado el archivo: {self.name}")
    
    def listar_archivo(self):
        arc_list = os.listdir(self.path)
        print("Files and directories in '", self.path, "' :") 

        for elemento in arc_list:
            ruta_completa = os.path.join(self.path, elemento)
            if os.path.isfile(ruta_completa):  # miramos si es fichero
                    print(elemento, ruta_completa, sep=', ')
    
    def eliminar_archivo(self):
        location = self.path
        path = os.path.join(location, self.name) 
        os.remove(path)

    def buscar_archivo(self):
        for dirpath, dirname, filename in os.walk(self.path):
            if self.name in filename:
                return f" this is the filepath:{os.path.join(dirpath, self.name)}"

    def mover_archivos(self,path_source, path_destination):
        get_files = os.listdir(path_source)

        for g in get_files:
            if self.name in g:
             shutil.move(path_source + self.name, path_destination)

    def renombrar_archivo(self,new_name):

        file_oldname = os.path.join(self.path, self.name)
        file_newname = os.path.join(self.path, new_name)

        os.rename(file_oldname, file_newname)

    def cambiar_permisos(self):
        perm = os.stat(self.name)
        print(f"Los permisos actuales del archivo son:{perm}")

        os.chmod(self.name, 0o755) #el segundo atributo son los permisos
        print(f"Los permisos nuevos del archivo son:{perm}")