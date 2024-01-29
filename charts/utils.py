FILE_DATA = '/Users/dandrade/Documents/Python course/Chatbot/data/data_et/data_processed.csv'

def filtrar_entidad(data, id):

    data_filt = list(filter(lambda contrats: contrats['nit_de_la_entidad'] == id, data))
    #print(len(data_filt))

    return data_filt

def filtrar_llaves(data):

    keys_s = ['fecha_firma_yyyymm', 'valor_contrato']

    data_with_date_value = [{key: value for key, value in dictionary.items() if key in keys_s} for dictionary in data]
    #print('*' * 50)
    #print("salida filtro data_with_date_values[0] de uttilites")
    #print('*' * 50)
    #print('\n')
    #print(data_with_date_value)
    return data_with_date_value

def total(data):

    values_by_date = {}

    for row in data:
        date = row['fecha_firma_yyyymm']
        value = float(row['valor_contrato'])
        #print(f" esto es date: {date}")
        #print(f" esto es value: {value}")
        #print(f" esto es values_by_date: {values_by_date}")
        if date in values_by_date:
            values_by_date[date] += value
        else:
            values_by_date[date] = value

    #print(f" esto es values_by_date: {values_by_date}")
    #print("Llega")
    #print('*' * 50)
    sorted_dates = sorted(values_by_date.keys())
    
    sorted_values_by_date = {key: values_by_date[key] for key in sorted_dates if key in values_by_date}
    #print(f" esto es sorted: {sorted_values_by_date}")
    #print('*' * 50)
    #print("salida de dict sorted_valuesby_date[0] de uttilites")
    #print('*' * 50)
    #print('\n')
    #print(f" esto es eso: {next(iter(sorted_values_by_date.items()))}")

    return sorted_values_by_date
