#ejemplo 4
import csv
import os
import shutil
import stat #proporciona constantes/funciones para interpretar los resultados de os.stat() y os.lstat(). Esta “estadística” proporciona los indicadores de permiso 
            #que necesitaremos para cambiar los permisos de archivo en el usuario, grupo u otros usuarios.

class directory:
    
    def __init__(self,name_directory, path_directory):

        self.name_directory = name_directory
        self.path_directory = path_directory       
    
    def crear_directorio(self):   
    
        path = os.path.join(self.path_directory, self.name_directory)
        os.mkdir(path)
        print("Directory '% s' created" % self.name_directory)
    
    def listar_directorio(self):

        dir_list = os.listdir(self.path_directory)
        print("Directories in '", self.path_directory, "' :") 

        for elemento in dir_list:
            ruta_completa_dir = os.path.join(self.path, elemento)
            if os.path.isdir(ruta_completa_dir):  # miramos si es fichero
                    print(elemento, ruta_completa_dir, sep=', ')

    def renombrar_directorio(self, new_name_directory):

        dir_oldname = os.path.join(self.path, self.name_directory)
        dir_newname = os.path.join(self.path, new_name_directory)

        os.rename(dir_oldname, dir_newname)  


"""
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
"""
"""
def leer_archivo(self,archivo):
    self.archivo = archivo

    try:  
        with open(archivo, 'r') as csvfile:
         reader_obj = csv.reader(csvfile)
         data = [row for row in reader_obj]
        return data   
    except FileNotFoundError:
        return []
   
def cargar_archivo(data):  
    with open("test5.csv", 'w' ,newline='') as csvfile:
        write_obj = csv.writer(csvfile)
        write_obj.writerow(data)

 
def agregar_equipo():
     
    data1 = input("Digiste el nombre del equipo")
    data2 = int(input("Digite el premio"))
    data3=  input("Digiste el puesto")
    data4=  input("Digiste el año en que gano")

    data.append([data1, data2, data3, data4])
    cargar_archivo(data)
    print(f"{data1} añadido a la lista /n")

def consultar():
     print("teams:")
     for team in data:
        print({f"{team[0]} | Money {team[1]} | Position {team[2]} | year {team[3]} "})  

def total():
    total_cash = sum(int(row[1]) for row in data)  
    print("El total es:", total_cash)

      
data = leer_archivo()
"""
"""
while True:
    n = int(input("Para registrar un premio pusle 1, Para consultar un premio pulse 2, Para calcular el toltal pulse 3, Desea salir del menu digite 4"))
    if n == 1 :
        agregar_equipo()
        continue
    if n == 2:
        consultar()
        continue
    if n == 3:
        total()
        continue      
    else:
        break        

    try:

    except Exception as e:
    print(f"Salio esto mal: {e}")
"""