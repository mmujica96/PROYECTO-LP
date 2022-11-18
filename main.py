import ply.lex as lex

import ply.lex as lex
#rust
#Palabras reservadas
reserved = {
  'let' : 'LET',
  'mut' : 'MUT',
  'const' : 'CONST',
  'for': 'FOR',
  'if': 'IF',
  'else': 'ELSE',
  'while': 'WHILE',
  'static': 'STATIC',
  'as': 'AS',
  'break': 'BREAK',
  'fn': 'FN',
  'println': 'PRINTLN',
  'main': 'MAIN',
  'return': 'RETURN',
  'asyn': 'ASYN',
  'away': 'AWAY',
  'continue': 'CONTINUE',
  'bool':'BOOL',
  'String':'TIPO_STRING',
  'from':'FROM'
}
#Agregue todos los tokens solicitados
tokens = [
  'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'RCOM',
  'LLLAV', 'RLLAV', 'ID','MACRO', 'LESS', 'GREAT', 'STRING', 'EQUAL', 'PUNTO_COMA','FLOTANTE','COMA','PUNTO',
  'TIPO_INT', 'TIPO_CHAR'
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
t_ignore_RCOM = r'\/\/.*'
t_LLLAV = r'\{'
t_RLLAV = r'\}'
t_MACRO=r'!'
t_LESS=r'\<'
t_GREAT=r'\>'
t_STRING=r'"[\S ]*"'
t_EQUAL=r'='
t_PUNTO_COMA= r';'
t_COMA=r','
t_PUNTO=r'\.'
t_TIPO_INT=r'^(iu|i)(8|16|32|64|128)'
t_TIPO_CHAR =r'\'\S\''

def t_NUMBER(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_FLOTANTE(t):
  r'\d+\.\d+'
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
#Lee el archivo source.txt y retorne los tokens
print("---------------------------------------\n")
print("---------A L G    # 1------------------\n")

with open("source.txt", "r") as archivo:
  lexer.input(archivo.read())
  archivo.seek(0)
  for linea in archivo:
    while True:
      tok = lexer.token()
      if not tok:
        break  # No more input
      print(tok)


print("---------------------------------------\n")
print("---------ALGORITMO #2------------------\n")

with open("source2.txt", "r") as archivo:
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



