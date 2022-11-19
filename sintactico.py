import ply.yacc as yacc
from lexico import tokens
##No es parte del analizador sintactico, corregir
def p_cuerpo(p):
  """cuerpo : print
  | asignacion"""

##No es parte del analizador sintactico, corregir
def p_print(p):
  """print : PRINTLN MACRO LPAREN valor RPAREN
  | PRINTLN LPAREN NUMBER RPAREN"""

##No es parte del analizador sintactico, corregir
def p_asignacion(p):
  """asignacion : LET ID EQUAL valor
  | LET MUT ID EQUAL valor
  | CONST ID EQUAL valor
  | LET ID TURBO_FISH TIPO_INT EQUAL NUMBER
  | LET ID TURBO_FISH TIPO_CHAR EQUAL CHAR
  | LET ID TURBO_FISH TIPO_STRING EQUAL STRING"""

##No es parte del analizador sintactico, corregir
def p_valor(p):
  """valor : NUMBER"""

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