import ply.lex as lex

import logging


logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

#rust
#Palabras reservadas
#AGREGAR LOS DATOS TIPOS FLOAT f8, f16....etc
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
  'bool':'TIPO_BOOL',
  'String':'TIPO_STRING',
  'from':'FROM',
  'new':'NEW',
  'Vec': 'VEC_OBJ',
  'vec' : 'VEC',
  'use' : 'USE',
  'char': 'TIPO_CHAR',
  'true' : 'TRUE',
  'false' : 'FALSE',
  'push' : 'PUSH',
  'pop' : 'POP',
  'enum' : 'ENUM',
  'in' : 'IN',
  'iter' : 'ITER'
}
#Agregue todos los tokens solicitados
tokens = [
  'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'RCOM','TIPO_INT',
  'LLLAV', 'RLLAV', 'ID','MACRONOT', 'LESS', 'GREAT', 'STRING', 'EQUAL', 'PUNTO_COMA','FLOAT','COMA','PUNTO', 'CHAR', 'TURBO_FISH', 'RCORCH',
   'LCORCH','BOOL', 'DOUBLE_POINT', 'AND', 'OR' #'NOT'
] + list(reserved.values())

#Agregue sus Expresiones Regulares y o Funciones
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore_RCOM = r'//[\S ]*'
t_LLLAV = r'\{'
t_RLLAV = r'\}'
t_MACRONOT=r'!'
t_LESS=r'\<'
t_GREAT=r'\>'
t_STRING=r'"[a-zA-Z]*"'
t_EQUAL=r'='
t_PUNTO_COMA= r';'
t_COMA=r','
t_PUNTO=r'\.'
t_CHAR =r'\'\S\''
t_TURBO_FISH=r'\:\:'
t_LCORCH=r'\['
t_RCORCH=r'\]'
t_DOUBLE_POINT=r'\:'
t_AND=r'\&'
#t_NOT=r'\!'
t_OR=r'\|' 


def t_TIPO_INT(t):
  r'(iu|i)(8|16|32|64|128|size)'
  return t

def t_BOOL(t):
  r'(true|false)'
  return t

def t_FLOAT(t):
  r'\d+\.\d+'
  return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value, 'ID')  # Check for reserved words
  return t

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
lexer = lex.lex(debug=True,debuglog=log)
#Lee el archivo source.txt y retorne los tokens

'''
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
      print(tok) '''