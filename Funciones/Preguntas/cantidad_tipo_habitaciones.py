# 4- ¿Cuál es la cantidad en cada barrio de determinado tipo de propiedad?

from Funciones.Generales import funciones_generales as fg

def cantidad_barrios(habitacion):
  """ Calcula y guarda las cantidades en cada barrio del tipo de habitacion elegida
      habitacion: tipo de habitacion elegida por el usuario """
  respuesta = {} # Diccionario: claves : nombres de los barrios; valores : cantidades del tipo de habitacion elegida

  # De acuerdo a los barrios disponibles se van generando las keys del diccionario con los contadores correspondientes inicializados en 0
  for barrio in fg.barrios_disponibles():
    respuesta[barrio] = 0

  for propiedad in fg.datos(): # Se recorre cada una de las entradas que contiene unicamente los datos necesarios para responder a la pregunta
    if habitacion in propiedad: # Si el tipo de habitacion que eligio el usuario se encuentra en esa entrada      
      for barrio in respuesta.keys(): # Se recorre cada uno de los barrios posibles
        if barrio in propiedad: #  Y se compara uno a uno con el barrio correspondiente a la entrada          
          respuesta[barrio] += 1 #  Hasta dar con el correcto y sumarle uno al contador indicado
  
  return respuesta
