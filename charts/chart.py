from charts import read_file
from charts import utils
import matplotlib.pyplot as plt

def graficar(id):

    try:

        data_from_file = read_file.leer_archivo(utils.FILE_DATA)

        data_filter_by_entity = utils.filtrar_entidad(data_from_file, id)

        data_with_keys = utils.filtrar_llaves(data_filter_by_entity)

        data_total_by_date = utils.total(data_with_keys)

        labels = data_total_by_date.keys()
        values = data_total_by_date.values()

        fig, ax = plt.subplots(figsize=(10,5)) #declarando variables, y figsize para el tamaño
        ax.bar(labels, values) #primero se pone el eje x y luego el y

        plt.title("Valores contrato firmado por año y mes") #Agregando titulo
        plt.xlabel("Fecha firma")
        plt.ylabel("Valores Contrato")

        plt.show()

        plt.savefig('Valores_de_contrar.png')
    except:
            print(f"The nit was not found")

if __name__ == "__main__":
     
    id = "832001871"
    graficar(id)
     