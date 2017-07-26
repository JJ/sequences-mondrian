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


import sys

from sequences_mondrian import Inspiration, PintaCuadro

## Programa principal

iterations= 5
width = 800
height = 1200
line_width = 4

TableauName= "Pi-Mondrian"

if len(sys.argv) > 1:
    iterations = sys.argv[1]
else:
    iterations = 5

Fichero = open("10000pi.txt")
Cadena= Fichero.read()
Fichero.close()

PI = list(Cadena)

array_of_cuadros = Inspiration(PI, iterations, width, height)
PintaCuadro(array_of_cuadros,iterations,TableauName,width,height,line_width)





