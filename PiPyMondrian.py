#!/usr/bin/python
#coding: utf-8

#       CopyRight 2013 Allan Psicobyte (psicobyte@gmail.com)
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, Image, ImageDraw


# Definición de clases y funciones

class SubRectangle:
    """crea un rectángulo con coordenadas y color como subdivisión de un rectágulo padre"""
    def __init__(self, orden, division, color, parent= None):

        self.Parent= parent
        self.Color= color

        if parent is None:
            self.ZeroX= 0
            self.ZeroY= 0
            self.EndX= WIDTH
            self.EndY= HEIGHT
            self.VorH= "V"
            self.Generation= 0

        else:

            self.Generation= parent.Generation + 1
            
            if parent.VorH == "V":
                self.VorH= "H"

                if orden == 1:
                    self.ZeroX= parent.ZeroX
                    self.ZeroY= parent.ZeroY
                    self.EndX= Division(parent.ZeroX, parent.EndX, division)
                    self.EndY= parent.EndY

                elif orden == 2:
                    self.ZeroX= Division(parent.ZeroX, parent.EndX, division)
                    self.ZeroY= parent.ZeroY
                    self.EndX= parent.EndX
                    self.EndY= parent.EndY

            elif parent.VorH == "H":
                self.VorH= "V"

                if orden == 1:
                    self.ZeroX= parent.ZeroX
                    self.ZeroY= parent.ZeroY
                    self.EndX= parent.EndX
                    self.EndY= Division(parent.ZeroY, parent.EndY, division)

                elif orden == 2:
                    self.ZeroX= parent.ZeroX
                    self.ZeroY= Division(parent.ZeroY, parent.EndY, division)
                    self.EndX= parent.EndX
                    self.EndY= parent.EndY



def DivideRectangle(sequence, array_of_cuadros, parent):
    """Toma los siguientes tres dígitos de Pi, y divide el cuadro en dos usando como proporción el primero de esos tres dígitos. Los otros dos digitos asignan el color de los cuadros """
 
    division= int(sequence.pop(0))
    color1= int(sequence.pop(0))
    color2= int(sequence.pop(0))

    array_of_cuadros.append(SubRectangle(1,division,color1,parent))
    array_of_cuadros.append(SubRectangle(2,division,color2,parent))


def Division(corta,larga,division):
    """Calcula el punto que coresponde a 'división' décimas partes entre 'corta' y 'larga' """

    if division == 0:
        resultado= larga

    else:
        resultado= corta + ((larga - corta) * division / 10)
        resultado= round(resultado,0)

    return resultado


def PintaCuadro(array_of_cuadros, generation,name):

    global WIDTH, HEIGHT, LINE

    img = Image.new("RGB", (WIDTH, HEIGHT), "#000000")

    draw = ImageDraw.Draw(img)

    for elemento in array_of_cuadros:

        if elemento.Color == 0:
            FillColor= "#FFFFFF"
        if elemento.Color == 1:
            FillColor= "#FFFFFF"
        if elemento.Color == 2:
            FillColor= "#FFFFFF"
        if elemento.Color == 3:
            FillColor= "#AA0000"
        if elemento.Color == 4:
            FillColor= "#AA0000"
        if elemento.Color == 5:
            FillColor= "#0000AA"
        if elemento.Color == 6:
            FillColor= "#0000AA"
        if elemento.Color == 7:
            FillColor= "#000000"
        if elemento.Color == 8:
            FillColor= "#000000"
        if elemento.Color == 9:
            FillColor= "#AAAA00"

        linea= round(LINE / 2,0)

        if elemento.Generation == generation:
            draw.rectangle([(elemento.ZeroX + linea, elemento.ZeroY + linea), (elemento.EndX - linea, elemento.EndY - linea)], outline="#000000", fill= FillColor)
    name = name + ".png"
    img.save(name, "PNG")


def Inspiration(sequence, Iterations):


    array_of_cuadros = []
    # Creamos el rectángulo raiz
    array_of_cuadros.append(SubRectangle(1,0,0))

    # Creamos el resto de rectángulos
    i = 0
    while i < Iterations:
        for elemento in array_of_cuadros:
            if elemento.Generation == i:
                DivideRectangle(sequence, array_of_cuadros, elemento)
        i = i + 1

    return array_of_cuadros



## Programa principal

iterations= 5

WIDTH= 1200
HEIGHT= 800

LINE= 4


TableauName= "PiPyMondrian"

if len(sys.argv) > 1:
    iterations = sys.argv[1]
else:
    iterations = 5

Fichero = open("10000pi.txt")
Cadena= Fichero.read()
Fichero.close()

PI = list(Cadena)

array_of_cuadros = Inspiration(PI, iterations)
PintaCuadro(array_of_cuadros,iterations,TableauName)





