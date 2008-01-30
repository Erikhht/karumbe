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

from ply import *
import tokenize

tokens = tokenize.tokens

precedence = (
               ('left', 'MAS','MENOS'),
               ('left', 'MULTIPLICADO','DIVIDIDO'),
               ('left', 'POTENCIA'),
               ('right','NEGATIVO')
)

def p_program(p):
    '''program : program statement
               | statement'''
    pass



def p_binary_operation(p):
    '''expresion : expresion MAS term
                 | expresion MENOS term
       termino   : termino MULTIPLICADO factor
                 | termino DIVIDIDO factor'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_number(p):
    '''number  : INTEGER
               | FLOAT'''
    p[0] = eval(p[1])


def p_number_signed(p): 
    '''number  : MENOS INTEGER
               | MENOS FLOAT'''
    p[0] = eval("-"+p[2])


def p_error(p):
    if not p:
        print "SYNTAX ERROR AT EOF"
  
  
bparser = yacc.yacc()


def parse(data):
    bparser.error = 0
    p = bparser.parse(data)
    if bparser.error: return None
    return p

