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

from spark import GenericParser

#   KaParser
#
#   El parseador es el que interpreta las partes o token que recibe
#   del kaTokenizer, basicamente aqui se define las reglas del lenguaje
#   en si y en el kaTokenizer las partes indivisibles (numeros, letras, puntuaciones, etc)
#   
#   
class kaParser(GenericParser):
    def __init__(self, start):
        GenericParser.__init__(self, start)

    def typestring(self, token):
        return token.type

    def error(self, token):
        print "Error de sintaxis `%s' (linea %s)" % (token, token.lineno)
        raise SystemExit   

    def p_funcdef(self, args):
        """
            funcdef ::= UN STRING TIENE parameters Y ES NEWLINE suite NEWLINE FIN
            funcdef ::= UN STRING ES NEWLINE suite NEWLINE FIN
        """
        print "Recognizing new function %s " % args[1]
    
    def p_parameters(self,args):
        """
            parameters ::= STRING
            parameters ::= STRING, parameters
        """
        pass