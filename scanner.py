# -*- coding: latin-1 -*-
############################################################################
#    Copyright (C) 2008 by crodas,czayas                                   #
#    mail@cesarodas.com, mail@carloszayas.com                              #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
############################################################################


import generic
GenericScanner = generic.GenericScanner
# Palabras reservadas
reserved = "un es y fin tiene repetir si".split(" ")


class Token():
    def __init__(self,tType,tValue):
        self.tType  = tType.upper()
        self.tValue = tValue.upper()
        print self.tType
        print "(%s)" % self.tValue
        print "---------------------------------"

#   Tokenizer
#   
#   Esta clase es la encargada de tokenizar el codigo fuente. La
#   accion de tokenizar es dividir at�micamente.
#   Ejemplo:
#           5+3*5
#           El tokenizador pasa al parseador 5,+,3,*,5 y el tipo de 
#           de operaci�n.
#
#   Este modulo hereda de la funcion Generic parser y la regla se
#   encuentra posterior a la definicion de la funcion
#   
class kaTokenizer(GenericScanner):
    def tokenize(self, input):
        self.rv = []
        GenericScanner.tokenize(self, input)
        return self.rv

    def t_new_line(self,s):
        r" [\n\;]"
        self.rv.append(Token('newline', s))
        
    def t_whitespace(self, s):
        r" [ \t\r]+ "
        pass

    
    #   Alphanumericos
    #
    #   Utilizados para nombre de funciones o variables, b�sicamente
    #   pueden ser desde una letra hasta n letras, pueden ser alfanumericos
    #   pero el primer caracter mandatoriamente debe ser una letra
    #   Los alfanumericos pueden ser caracteres especiales del alfabeto espa�ol
    def t_alphanums(self, s):
        r" [a-zA-Z���������?��������??][ \t\r\n]|[a-zA-Z���������?��������??][a-zA-Z0-9���������?��������??]+"
        s = s.strip()
        #   Verificar si lo que leimos es una palabra reservada
        if ( s.lower() in reserved) :
            self.rv.append(Token(s, s))
        else:
            self.rv.append(Token('string', s))
    
    #   Operaciones matematicas
    #   
    #   Las operaciones matematicas soportadas son
    #   suma, resta, multiplicacion, division y potenciacion.
    def t_op(self,s):
        r" \+ | \* | \/ | \- | \*\*"
        self.rv.append(Token('op', s))
    
    #   Parentesis
    def t_lp(self,s):
        r" \( "
        self.rv.append(Token('lp', s))
    
    #   Parentesis
    def t_rp(self,s):
        r" \) "
        self.rv.append(Token('rp', s))
    
    #   Numeros flotantes
    def t_float(self,s):
        r" \d+ \. \d+ "
        self.rv.append(Token('number', s))
    
    #   Numeros decimales      
    def t_number(self,s):
        r" \d+ " 
        self.rv.append(Token('number', s))


