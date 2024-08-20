# Módulos
from Funciones.Preguntas import promedios_barrios as p1
from Funciones.Preguntas import promedios_tipo_habitaciones as p2
from Funciones.Preguntas import cantidad_barrios as p3
from Funciones.Preguntas import cantidad_tipo_habitaciones as p4

from Funciones.Generales import funciones_gráfico as gr
from Funciones.Generales import funciones_generales as fg

habitaciones = fg.habitaciones_disponibles() # Se guardan los tipos de habitaciones disponibles
barrios = fg.barrios_disponibles() # lo mismo pero con los barrios

directorio = 'Datos/'
cambiar_fase_1 = False
cambiar_fase_2 = False

fg.limpiar()
# Bucle principal, este se utiliza para mantener al usuario dentro hasta que los valores que ingrese sean los correectos
while True:
    # Primera fase = el usuario tiene que elegir por qué quiere filtrar
    # Cantidad = Preguntas 3 y 4; Promedios = Preguntas 1 y 2
    if not cambiar_fase_1:
        usuario = input('Eligir qué quiere filtrar: \n[1] Cantidad\n[2] Promedios\n\nRespuesta: ')
        for i in range(1, 3):
            if str(i) == usuario:
                salir = True
                break
            else:
                salir = False

        fg.limpiar() # Se limpia la consola
        if salir: # Si el usuario ingresa un valor correcto, se sigue a la siguiente fase
          cambiar_fase_1 = True
          
          if usuario == '1': cantidad = True # Si determina si se elegió cantidad o promedios
          else: cantidad = False
        else: 
          print('Eligió una opción incorrecta. Vuelva a intentar.\n')

    # Siguiente fase: se le pregunta al usuario por qué opción quiere filtrar: tipo de habitación o barrio      
    elif not cambiar_fase_2:
        usuario = input('Elegir por que opción quiere filtrar: \n[1] Tipo de habitación\n[2] Barrio\n\nRespuesta: ')
        for i in range(1, 3):
            if str(i) == usuario:
                salir = True
                break
            else:
                salir = False
        
        # Mimso procemiento que arriba
        fg.limpiar()
        cambiar_fase_2 = True if salir else print('Eligió una opción incorrecta. Vuelva a intentar.\n')

    else:
        # Primera y cuarta pregunta
        if usuario == '1':
            print('Elegir un tipo de habitación disponible:')
            habitacion, salir = fg.existe(habitaciones)
            if salir:
              if cantidad: # cuarta pregunta
                cantidad_barrios = p4.cantidad_barrios(habitacion) # se guarda la cantidad por barrio
                fg.limpiar()
                # se grafica la pregunta
                gr.graficar_pregunta(cantidad_barrios, 'Barrios', 'Cantidad', 'Cantidad x Barrios / ' + str(habitacion))
                break
              else: # primera pregunta
                promedios_barrios = p1.promedios_barrios(habitacion) # se guardan los promedios por barrio
                fg.limpiar()
                # se grafica la pregunta
                gr.graficar_pregunta(promedios_barrios, 'Barrios', 'Promedios', 'Promedios x Barrios / ' + str(habitacion))
                break
            else:
                fg.limpiar()
                print('Tipo de habitación no disponible. Inténtelo de nuevo.\n')

        # Segunda y tercera pregunta
        elif usuario == '2':
            print('Elegir un barrio disponible: ')
            barrio, salir = fg.existe(barrios)
            if salir:
              if cantidad: # tercera pregunta
                cantidad_habitaciones = p3.cantidad_habitaciones(barrio) # se guarda la cantidad por tipo de habitación
                fg.limpiar()
                # se grafica la pregunta
                gr.graficar_pregunta(cantidad_habitaciones, 'Tipos de habitaciones', 'Cantidad', 'Cantidad x Tipos de habtaciones / ' + str(barrio)) 
                break
              else: # segunda pregunta
                fg.limpiar()
                promedios_habitaciones = p2.tipo_habitaciones_promedios(barrio) # se guardan los promedios por tipos de habitación
                # se grafica la pregunta
                gr.graficar_pregunta(promedios_habitaciones, 'Tipos de habitaciones', 'Promedios', 'Promedios x Tipos de habtaciones / ' + str(barrio))
                break
            else:
                fg.limpiar()
                print('Barrio no disponible. Inténtelo de nuevo.\n')
