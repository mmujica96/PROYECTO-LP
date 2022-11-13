import ply.lex as lex

import ply.lex as lex
#rust
#Agregue todas las palabras reservadas
reserved = {
  'for': 'FOR',
  'if': 'IF',
  'else': 'ELSE',
  'while': 'WHILE',
  'let': 'LET',
  'static': 'STATIC',
  'as': 'AS',
  'break': 'BREAK',
  'fn': 'FN',
  'println': 'PRINTLN',
  'main': 'MAIN',
}
#Agregue todos los tokens solicitados
tokens = [
  'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'RCOM',
  'LCORCH', 'RCORCH', 'ID','MACRO', 'LESS', 'GREAT', 'STRING', 'EQUAL'
] + list(reserved.values())


def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')  # Check for reserved words
  return t

#Agregue sus Expresiones Regulares y o Funciones
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_RCOM = r'//'
t_LCORCH = r'\{'
t_RCORCH = r'\}'
t_MACRO=r'!'
t_LESS=r'\<'
t_GREAT=r'\>'
t_STRING=r'"'
t_EQUAL=r'='

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

#Agregue conteo de lineas
def t_newline(t):
  r';+'
  t.lexer.lineno += len(t.value)

#Agregue token de ignorar
t_ignore = (' \n')

#Agregue token de error
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

#Construya el lexer
lexer = lex.lex()
#Lea el archivo source.txt y retorne los tokens

with open("source.txt", "r") as archivo:
  lexer.input(archivo.read())
  archivo.seek(0)
  for linea in archivo:
    while True:
      tok = lexer.token()
      if not tok:
        break  # No more input
      print(tok)
"""
data = '''fn main(){
println!("Hola mundo");
//Este es un comentario
}
'''
print('Mi primer Lexer')
lexer.input(data)

# Tokenize
while True:
  tok = lexer.token()
  if not tok:
    break  # No more input
  print(tok)
"""