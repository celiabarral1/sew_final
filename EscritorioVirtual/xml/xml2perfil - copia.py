#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Celia
#
# Created:     10/12/2023
# Copyright:   (c) Celia 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

archivo_1 = 'perfil1.svg'
archivo_2 = 'perfil2.svg'
archivo_3 = 'perfil3.svg'
archivoXML= 'rutasEsquema.xml'

def prologo_svg(nombre):
    with open(nombre, 'w') as archivoKML:
        archivoKML.write('<?xml version="1.0" encoding="UTF-8" ?>\n')
        archivoKML.write('<svg xmlns="http://www.w3.org/2000/svg" version="2.0" height="180" width="500">\n')

def altimetria(archivoXML):
 try:
    arbol = ET.parse(archivoXML)
    raiz = arbol.getroot()
    ns = {'ns': 'http://www.uniovi.es'}
    rutas = raiz.findall('.//ns:ruta',ns)

    altitud_inicial=rutas[0].find('.//ns:altitud',ns).text
    d_inicial=10


    for i in range(0,len(rutas)):
        ruta = rutas[i]
        hitos_por_ruta = ruta.findall('.//ns:hito',ns)
        if i == 0:
            archivo_1 = open('perfil1.svg', 'a')
        elif i == 1:
            archivo_1 = open('perfil2.svg', 'a')
        elif i == 2:
            archivo_1 = open('perfil3.svg', 'a')
         # Crear la polilínea con los puntos de altitud y distancia
        puntos = []
        distancia = 0
        for hito in ruta.findall('.//ns:hito',ns):
            altitud_hito = int(hito.find('.//ns:altitud',ns).text)
            distancia_hito = int(hito.find('.//ns:distancia',ns).text)
            distancia += distancia_hito
            puntos.append((distancia, altitud_hito))

        # Escribir la polilínea en el archivo SVG
        polyline_points = ' '.join([f'{x},{y}' for x, y in puntos])
        archivo_1.write(f'<polyline points="{polyline_points}" style="fill:white;stroke:red;stroke-width:4" /> \n')
        archivo_1.write('</svg>')


    archivo_1.close()
 except IOError:
    print ('No se encuentra el archivo ', archivoXML)
    exit()
 except ET.ParseError:
    print("Error procesando en el archivo XML = ", archivoXML)
    exit()




def main():
    prologo_svg(archivo_1)
    prologo_svg(archivo_2)
    prologo_svg(archivo_3)
    altimetria('rutasEsquema.xml')

if __name__ == '__main__':
    main()
