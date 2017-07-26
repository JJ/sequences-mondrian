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

def fib(n):
    return reduce( lambda prev,this: prev+ [prev[-2]+prev[-1]], range(1,n+1), [1,1])

## Programa principal
iterations= 5
width = 800
height = 1200
line_width = 4

iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 5
fib_0 = sys.argv[2] if len(sys.argv) > 2 else 1
fib_1 = sys.argv[3] if len(sys.argv) > 3 else 1
TableauName= "Fib-"+str(fib_0)+"-"+str(fib_1)+"-Mondrian"

size = sum(map( lambda n: 2**n, range(0,iterations)))
fibonacci_sequence = fib( size *3 )

array_of_cuadros = Inspiration(fibonacci_sequence, iterations, width, height)
PintaCuadro(array_of_cuadros,iterations,TableauName,width,height,line_width)





