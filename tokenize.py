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

keywords = (
    'REPETIR','UN','TIENE','Y','ES','FIN','VECES','COMMENT','MLCOMMENT'
) 


tokens = keywords + (
     'PLUS','MINUS','TIMES','DIVIDE','POWER',
     'LPAREN','RPAREN','LT','LE','GT','GE','NE',
     'COMMA','SEMI', 'INTEGER','FLOAT', 'STRING',
     'ID','NEWLINE'
)

t_ignore = ' \t'

def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t
    
def t_MLCOMMENT(t):
    r' /\*(.|\n)*?\*/'   
    return t
   
def t_COMMENT(t):
    r'\#s.*'
    return t

    

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_POWER   = r'\^'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LT      = r'<'
t_LE      = r'<='
t_GT      = r'>'
t_GE      = r'>='
t_NE      = r'<>'
t_COMMA   = r'\,'
t_SEMI    = r';'
t_INTEGER = r'\d+'    
t_FLOAT   = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_STRING  = r'\".*?\"'

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print "Letra(", t.value[0],") no reconocida, Linea ",t.lexer.lineno
    t.lexer.skip(1)

f = lex.lex()
