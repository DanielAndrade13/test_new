import nltk
from modules.nl_processing import Nlp
from modules.directory_operations import Directory
from modules.file_operations import File
import os
from charts import chart
from data import manage_db


def run_chatbot(chat):
    """
        Manejador de ejecución de chatbot haciendo uso de modelos implementados
        
        Args: 
            chat (str): Objeto instanciado de la clase Nlp   
            
        Returns:
            None
    """
               
    try:
        flag = True
        chat.talk_to_client(f"My name is {chat.BOT_NAME}. I will answer your queries about file and directory manipulation .")
        while flag:
            chat.talk_to_client("Please type a request about files and directories. If you want to exit, type Bye!")
            user_response = input()
            if "bye" in user_response.lower():
                flag = False
                chat.talk_to_client("Bye! take care..")
            elif "thank" in user_response.lower():
                flag = False
                chat.talk_to_client("You are welcome..")
            elif chat.greeting(user_response) is not None:
                chat.talk_to_client(chat.greeting(user_response))
            else:
                tokens = nltk.word_tokenize(user_response)
                chat.talk_to_client(chat.response(user_response))
                if 'list files' in user_response:
                    print(chat.directory.listar_archivo())
                elif 'create file' in user_response:
                    name = tokens[tokens.index('file') + 1]
                    chat.directory.crear_archivo(name)
                elif 'create directory' in user_response:
                    name = tokens[tokens.index('directory') + 1]
                    chat.directory.crear_directorio(name)
                elif 'list directories' in user_response:
                    print(chat.directory.listar_directorio())
                elif 'rename directory' in user_response:
                    old_name = tokens[tokens.index('directory') + 1]
                    new_name = tokens[tokens.index('to') + 1]
                    chat.directory.renombrar_directorio(old_name, new_name)  

                elif 'rename file' in user_response:
                    old_name = tokens[tokens.index('file') + 1]
                    new_name = tokens[tokens.index('to') + 1]
                    #f = chat.directory.path_directory
                    #print(f"Esto sale de {f} ")               
                    file = File(chat.directory.path_directory)
                    #print(f" esto es old: {old_name}")
                    #print(f" esto es old: {new_name}")
                    file.renombrar_archivo(old_name, new_name)   

                elif 'delete file' in user_response:
                    name = tokens[tokens.index('file') + 1]
                    file = File(chat.directory.path_directory)
                    file.eliminar_archivo(name)

                elif 'search' in user_response or 'find' in user_response or 'lookup' in user_response:
                    search_keywords = ['search', 'find', 'lookup']
                    #name = tokens[tokens.index('search') + 1]
                    name = tokens[tokens.index(next((word for word in tokens if word in search_keywords), None)) + 1] if any(word in tokens for word in search_keywords) else None
                    chat.directory.listar_archivo(name)
                    
                elif 'move file' in user_response:
                    tokens = user_response.split()
                    # Encontrar los índices de las palabras clave "file" y "to"
                    move_index = tokens.index("file")
                    to_index = tokens.index("to")
                    file_name = " ".join(tokens[move_index + 1:to_index])
                    dir_name = " ".join(tokens[to_index + 1:])

                    #print(f" This is file_path: {file_name}")
                    #print(f" This is destination_path: {dir_name}")

                    #file_path = os.path.join(chat.directory.path_directory, file_name)
                    destination_path = os.path.join(chat.directory.path_directory, dir_name)

                    #print(f" This is file_path: {file_path}")
                    #print(f" This is destination_path: {destination_path}")

                    chat.directory.mover_archivo(file_name, destination_path)

                elif 'change permissions' in user_response:
                    tokens = user_response.split()
                    # Encontrar los índices de las palabras clave "move" y "to"
                    name = tokens.index("permissions")
                    to_index = tokens.index("to")
                    #file_path = " ".join(tokens[name + 1:to_index])
                    name = tokens[tokens.index('permissions') + 1]
                    #print (f"Esto es name:{name}")
                
                    permissions = int(" ".join(tokens[to_index + 1:]), 8)
                    #print (f"Esto es permissions:{permissions}")

                    file = File(os.path.join(chat.directory.path_directory, name))
                    file.cambiar_permisos(permissions)

                elif 'graphic' in user_response:
                    entity_select = tokens[tokens.index('entity') + 1]
                    chart.graficar(entity_select)

                elif 'data base' in user_response:
                    manage_db.escribir_bd()

    except LookupError as err:
        print ('Tenemos un error',err)    
        
        
if __name__ == '__main__':
    
    directory_path = r'/Users/dandrade/Documents/Python course/Chatbot/data/data_test'
    #print(directory_path)

    #obtener la ruta absoluta del directorio.
    absolute_path = os.path.abspath(directory_path)
    
    #Instanciando objeto de tipo Directory
    directory = Directory(absolute_path)

    #Ruta con corpus usado para entrenar el modelo
    path_corpus = '/Users/dandrade/Documents/Python course/Chatbot/modules/files_directories.txt'  
    
    #Instanciando objeto de tipo Nlp
    chatbot = Nlp(directory, path_corpus)
    print('Intanciado objeto')
    chatbot.initialize_nlp()
    print('Inicializado modulo nlp')
    run_chatbot(chatbot)
    print('Chat finalizado')