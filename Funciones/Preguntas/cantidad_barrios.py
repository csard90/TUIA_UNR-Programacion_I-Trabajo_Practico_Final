# 3- ¿Cuál es la cantidad de tipos de propiedad de determinado barrio?

from Funciones.Generales import funciones_generales as fg

def cantidad_habitaciones(barrio):
  """ Calcula y guarda las cantidades de cada tipo de habitacion del barrio elegido
      barrio: barrio elegido por el usuario """
 
  respuesta = {} # Diccionario: claves : tipos de habitaciones ; valores : cantidades de cada tipo en el determinado barrio
  
  # De acuerdo a los tipos de habitaciones disponibles se van generando las keys del diccionario con los contadores correspondientes inicializados en 0
  for tipo in fg.habitaciones_disponibles():
    respuesta[tipo] = 0

  for propiedad in fg.datos(): # Se recorre cada una de las entradas que contiene unicamente los datos necesarios para responder a la pregunta        
    if barrio in propiedad: # Si el barrio que eligio el usuario se encuentra en esa entrada      
      for tipo in respuesta.keys(): # Se recorre cada tipos de habitaciones posibles
        if tipo in propiedad: #  Y se compara uno a uno con el tipo de propiedad correspondiente a la entrada          
          respuesta[tipo] += 1 #  Hasta dar con el correcto y sumarle uno al contador indicado

  return respuesta
