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
    def __init__(self, orden, division, color, width, height, parent= None):

        self.Parent= parent
        self.Color= color

        if parent is None:
            self.ZeroX= 0
            self.ZeroY= 0
            self.EndX= width
            self.EndY= height
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



def DivideRectangle(sequence, array_of_cuadros, parent, width, height):
    """Toma los siguientes tres dígitos de Pi, y divide el cuadro en dos usando como proporción el primero de esos tres dígitos. Los otros dos digitos asignan el color de los cuadros """

    print( "Tamaño ", len(sequence), "\n")
    division= int(sequence.pop(0)) % 10
    color1= int(sequence.pop(0)) % 10
    color2= int(sequence.pop(0)) % 10 

    array_of_cuadros.append(SubRectangle(1,division,color1, width, height, parent))
    array_of_cuadros.append(SubRectangle(2,division,color2, width, height, parent))


def Division(corta,larga,division):
    """Calcula el punto que coresponde a 'división' décimas partes entre 'corta' y 'larga' """

    if division == 0:
        resultado= larga

    else:
        resultado= corta + ((larga - corta) * division / 10)
        resultado= round(resultado,0)

    return resultado


def PintaCuadro(array_of_cuadros, generation, name, width,height,line_width):

    colores = [ ("#FFFFFF","blanco"),("#FFFFFF","blanco"),("#FFFFFF","blanco"),
                ("#AA0000","rojo"),("#AA0000","rojo"),
                ("#0000AA","azul"),("#0000AA","azul"),
                ("#000000","negro"),("#000000","negro"),
                ("#AAAA00","verde") ]
    
    img = Image.new("RGB", (width, height), "#ffffff")
    linea = round(line_width/2.0)
    draw = ImageDraw.Draw(img)    
    for elemento in array_of_cuadros:
        indice = elemento.Color 
        FillColor= colores[indice][0]
        if elemento.Generation == generation:
            draw.rectangle([(elemento.ZeroX + linea, elemento.ZeroY + linea), (elemento.EndX - linea, elemento.EndY - linea)], outline="#000000")
            draw.text((elemento.ZeroX + linea + 1,elemento.ZeroY + linea),colores[indice][1],fill=FillColor)

    name = name + ".png"
    img.save(name, "PNG")


def Inspiration(sequence, Iterations, width, height):


    array_of_cuadros = []
    # Creamos el rectángulo raiz
    base = SubRectangle(1, 0, 0, width, height)
    array_of_cuadros.append(base)

    # Creamos el resto de rectángulos
    i = 0
    while i < Iterations:
        print("Iteration ", i )
        for elemento in array_of_cuadros:
            if elemento.Generation == i:
                DivideRectangle(sequence, array_of_cuadros, elemento, width, height)
        i = i + 1

    return array_of_cuadros








