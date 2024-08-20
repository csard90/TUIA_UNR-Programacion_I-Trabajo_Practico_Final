# Librerías para gráficos
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

directorio = 'Gráficos/'

def graficar_pregunta(diccionario, tituloX, tituloY, titulo):
    """ Grafica la pregunta
        diccionario: diccionario con los datos que se van a graficar; títuloX = título del eje X; títuloY = título del eje Y; título = título de todo el gráfico """
    plt.figure(figsize= (16, 6)) # Tamaño del gráfico
    plt.bar(diccionario.keys(), diccionario.values()) # Estilo del gráfico; bar = barras
    plt.xticks(rotation = 90, fontsize = 12, fontfamily = 'sans', color = 'RebeccaPurple') # Tamaño de la letra del eje X
    plt.yticks(fontsize = 12, fontfamily = 'sans', color = 'RebeccaPurple') # Tamaño de la letra del eje Y
    plt.xlabel(tituloX, fontsize = 18, fontweight = 'bold', fontfamily = 'serif') # Título del eje X
    plt.ylabel(tituloY, fontsize = 18, fontweight = 'bold', fontfamily = 'serif') # Título del eje Y
    plt.suptitle(titulo, fontsize = 26, fontweight = 'bold', fontfamily = 'serif') # Título del gráfico
    plt.savefig(directorio + tituloY + '_' + tituloX + '.png', bbox_inches = 'tight') # Guarda la imagen como .png