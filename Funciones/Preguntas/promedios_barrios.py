#1- ¿Cuál es el precio medio en cada barrio según el tipo de propiedad?

from Funciones.Generales import funciones_generales as fg 
import csv

directorio = 'Datos/'

def promedios_barrios(tipo):
    """ Calcula y guarda los promedios en cada barrio de un tipo de habitación elegido
        tipo: tipo de habitación escogido por el usuario """
    barrios = {} # Diccionario: claves : nombres de los barrios; valores : listas de precios
    promedios_barrios = {} # Diccionario: claves : nombres de barrios; valores : promedios de cada barrio

    # Se recorre el .csv en busca de los precios
    with open(directorio + 'listings.csv', newline='', encoding='utf-8') as File:
        reader = csv.reader(File, delimiter=',')
        for row in reader:
            # Detecta el número de la columna 'room_type', 'price' y 'neighbourhood_cleansed'
            if 'room_type' in row and 'price' in row and 'neighbourhood_cleansed' in row:
                num_columna_tipo = fg.numero_columna(row, 'room_type')
                num_columna_precio = fg.numero_columna(row, 'price')
                num_columna_barrio = fg.numero_columna(row, 'neighbourhood_cleansed')
            else: 
            # Después del header
                if row[num_columna_tipo] == tipo: # Si el tipo que eligió el usuario coincide con el tipo que tiene la fila, se guarda su precio y barrio
                    barrio = row[num_columna_barrio]
                    precio = float(row[num_columna_precio][1:].replace(',','')) # Se elimina el símbolo $ y se borran las ','

                    if precio != 0: # Si el precio es igual a cero no se guarda directamente
                        # Si el barrio no se encuentra en el diccionario, se lo guarda por primera vez con una lista con un primer precio
                        if not barrios.get(barrio): barrios[barrio] = [precio] 
                        # En caso de ya existir se le añade a la lista otro precio
                        else: barrios[barrio].append(precio)
    
    promedios_barrios = fg.promedio(barrios) # Se calcula el promedio por cada barrio

    return promedios_barrios

