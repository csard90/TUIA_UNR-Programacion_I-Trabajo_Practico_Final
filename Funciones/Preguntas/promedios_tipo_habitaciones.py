#2- ¿Cuál es el precio medio por cada tipo de propiedad en un determinado barrio?

from Funciones.Generales import funciones_generales as fg
import csv

directorio = 'Datos/'

def tipo_habitaciones_promedios(barrio):
    """ Calcula y guarda los promedios de cada unos de los tipos de habitaciones en el barrio elegido
        barrio = barrio escogido por el usuario """
    tipo_habitaciones = {} # Diccionario: claves : nombres de los tipos de habitaciones; valores : listas de precios
    tipo_habitaciones_promedios = {} # Diccionario: claves : nombre de los tipos de habitaciones; valores = promedio de cada tipo de habitacion

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
                if row[num_columna_barrio] == barrio: # Si el barrio que eligió el usuario coincide con el tipo que tiene la fila, se guarda su precio y tipo
                    tipo_habitacion = row[num_columna_tipo]
                    precio = float(row[num_columna_precio][1:].replace(',','')) # Se elimina el símbolo $ y se sacan las ','

                    if precio != 0: # Si el precio es igual a cero no se guarda directamente
                        # Si el tipo de habitacion no se encuentra en el diccionario, se lo guarda por primera vez con una lista con un primer precio
                        if not tipo_habitaciones.get(tipo_habitacion): tipo_habitaciones[tipo_habitacion] = [precio]  
                        # En caso de ya existir se le añade a la lista otro precio
                        else: tipo_habitaciones[tipo_habitacion].append(precio)

    tipo_habitaciones_promedios = fg.promedio(tipo_habitaciones) # Se calcula el promedio de cada tipo
    return tipo_habitaciones_promedios