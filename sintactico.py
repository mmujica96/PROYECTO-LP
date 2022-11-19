import ply.yacc as yacc
from lexico import tokens
##No es parte del analizador sintactico, corregir
def p_cuerpo(p):
  """cuerpo : print
  | asignacion
  | tupla_asignacion
  | tupla_declaracion"""

##No es parte del analizador sintactico, corregir
def p_print(p):
  """print : PRINTLN MACRO LPAREN valor RPAREN
  | PRINTLN LPAREN NUMBER RPAREN"""

def p_tupla_asignacion(p):
  """tupla_asignacion : LPAREN tupla_lista_de_datos RPAREN
  """

##No es parte del analizador sintactico, corregir
def p_asignacion(p):
  """asignacion : LET ID EQUAL valor
  | LET MUT ID EQUAL valor
  | CONST ID EQUAL valor
  | LET ID DOUBLE_POINT TIPO_INT EQUAL NUMBER
  | LET ID DOUBLE_POINT TIPO_CHAR EQUAL CHAR
  | LET ID DOUBLE_POINT TIPO_STRING EQUAL STRING
  | LET MUT ID EQUAL tipo_de_dato TURBO_FISH NEW LPAREN RPAREN
  | LET ID DOUBLE_POINT tupla_asignacion EQUAL tupla_declaracion
  | LET ID EQUAL tupla_declaracion
  """

def p_tupla_declaracion(p):
  """tupla_declaracion : LPAREN tupla_valores RPAREN"""

def p_tupla_lista_de_datos(p):
  """tupla_lista_de_datos : tipo_de_dato
  | tipo_de_dato COMA tupla_lista_de_datos"""

def p_tupla_valores(p):
  """tupla_valores : valor
  | valor COMA tupla_valores """

def p_tipo_de_dato(p):
  """tipo_de_dato : TIPO_STRING
  | TIPO_BOOL
  | TIPO_CHAR
  | TIPO_INT"""

##No es parte del analizador sintactico, corregir
def p_valor(p):
  """valor : NUMBER
  | STRING
  | CHAR
  | BOOL
  | FLOAT"""

##No es parte del analizador sintactico, corregir
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
 # Build the parser
parser = yacc.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)

while True:
  try:
    s = input('calc > ')
  except EOFError:
    break
  if not s: continue
  validaRegla(s)

'''Ejemplos que por ahora puede validar
a=20
variable=30.2
imprimir(var)
imprimir(20.3)
'''

'''
Para practicar implemente las siguientes reglas:
a=30+23
var=20-310*292/23
cond=20>variable
if var>10: imprimir(True)
'''