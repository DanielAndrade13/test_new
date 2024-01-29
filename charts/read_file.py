import csv

def leer_archivo(path):

    #path = r'/Users/dandrade/Documents/Python course/Chatbot/data/data_et/data_processed.csv'
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader)
                
        data = []

        for line in reader:
            iterable = zip(header, line)
            dic_in_line = {key : value for key, value in iterable}

            data.append(dic_in_line)

        #print('*' * 50)
        #print("Slida data[0] de lectura")
        #print('*' * 50)
        #print('\n')
        #print(data[0])

    return data