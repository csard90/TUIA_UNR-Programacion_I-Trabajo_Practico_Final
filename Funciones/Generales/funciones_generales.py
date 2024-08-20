# Librerías y módulos
import csv
import os

directorio = 'Datos/'

# Limpiar la consola
def limpiar():
    # Se imprime en la consola, dependiendo del S.O., un comando para limpiarla
    os.system("cls") if os.name == "nt" else os.system("clear") # nt = Windows

def numero_columna(fila, columna):
    """ Retorna el indice de una columna en específico
        fila: una fila del .csv; columna: nombre de la columna que se quiere buscar """
    num_columna = 0
    for i in fila:
        # cuando el valor del elemento i coincida con el nombre que se busca (columna), se rompe el bucle y se devuelve el contador con el indice
        if not i == columna: num_columna += 1 
        else: break

    return num_columna

def habitaciones_disponibles(): 
    """ Verifica y retorna los tipos de habitaciones que puede elegir el usuario """
    tipo_habitacion = [] # Se guadan estos tipos en una lista

    # Se revisa el csv buscando todos los tipos de habitaciones
    with open(directorio + 'listings.csv', newline='', encoding='utf-8') as File:
        reader = csv.reader(File, delimiter=',')
        for row in reader:
            # Detecta el número de la columna 'room_type'
            if 'room_type' in row: num_columna = numero_columna(row, 'room_type')
            else:
            # Guarda en una lista todos los tipos de habitaciones disponibles sin repetir
                if not row[num_columna] in tipo_habitacion: tipo_habitacion.append(row[num_columna])

    return tipo_habitacion

def barrios_disponibles(): 
    """ Verfica los barrios disponibles que el usuario puede elegir """
    barrios_disponibles = []

    # Se revisa el csv buscando todos los barrios disponibles
    with open(directorio + 'listings.csv', newline='', encoding='utf-8') as File:
        reader = csv.reader(File, delimiter=',')
        for row in reader:
            # Detecta el número de la columna 'neighbourhood_cleansed'
            if 'neighbourhood_cleansed' in row: num_columna = numero_columna(row, 'neighbourhood_cleansed')
            else:
            # Guarda en una lista todos los barrios disponibles sin repetir
                if not row[num_columna] in barrios_disponibles: barrios_disponibles.append(row[num_columna])

    return barrios_disponibles


def promedio(valores):
    """ Calcula y retorna los promedios de los valores guardados en un diccionario
        valores: diccionario con que contiene como valor una lista de precios """
    promedio_valores = {} # Diccionario para guardar los promedios
    for llave, valor in valores.items():
        suma_valores = sum(valor) # Se suman todos los precios de la lista

        promedio_valores[llave] = round(suma_valores/len(valor), 2) # Se calcula el promedio y se redondean los decimales a dos dígitos
        
    return promedio_valores


def existe(valores):
    """ Imprime valores (opciones) por pantalla, permite al usuario elegir entre uno de ellos y valida que exista o no la respuesta entre las disponibles
        valores: lista con nombres (str) """
    # Se imprimen en pantalla todos los valores que el usuario puede elegir
    for i in range(len(valores)):
        print('['+ str(i + 1) +']', valores[i])
    usuario = input('\nRespuesta: ') # Se le pide al usuario que ingrese un valor

    # Bucle para validar si el valor ingresado por el usuario este dentro del rango de valores disponibles
    for i in range(len(valores)):
        # Si es así, se le da a la variable del usuario el valor que eligió (nombre de barrio o tipo de habitación)
        if usuario == str(i + 1):
            usuario = valores[i]
            salir = True
            break
        
        else:
            salir = False
    
    return usuario, salir

def datos():
    """ Extrae del csv unicamente los datos necesarios para responder a las preguntas 3 y 4 y las guarda en una lista de listas"""
  
    datos = []
  
    with open(directorio + 'listings.csv', newline='', encoding='utf-8') as File:  
        reader = csv.reader(File, delimiter=',')    
        for row in reader:           

          if 'neighbourhood_cleansed' in row and 'room_type' in row:
              num_columna_barrio = numero_columna(row, 'neighbourhood_cleansed')
              num_columna_tipo = numero_columna(row, 'room_type')

          else:        
              datos.append([ row[num_columna_barrio] , row[num_columna_tipo] ])      

    return datos