import ply.yacc as yacc
from lexico import tokens

def p_cuerpo(p):
  """cuerpo : asignacion
            | operaciones
            | comparaciones
            | definir_funcion
            | print
            | library_call"""

##ASIGNACION - HANS RAMOS

## problema haciendo una regla que englobe (let , let mut, const) en una sola llamada asignacion, arreglar
def p_asignacion(p):
  """asignacion : LET ID DOUBLE_POINT VEC_OBJ LESS tipo_de_dato GREAT EQUAL VEC MACRO LCORCH tupla_valores RCORCH
                | LET ID EQUAL VEC MACRO LCORCH tupla_valores RCORCH
                | LET ID EQUAL VEC TURBO_FISH NEW LPAREN RPAREN
                | LET ID EQUAL VEC MACRO LCORCH RCORCH
                | LET ID EQUAL valor
                | LET MUT ID EQUAL valor
                | CONST ID EQUAL valor
                | LET ID DOUBLE_POINT TIPO_INT EQUAL NUMBER
                | LET ID DOUBLE_POINT TIPO_CHAR EQUAL CHAR
                | LET ID DOUBLE_POINT TIPO_STRING EQUAL STRING
                | LET MUT ID EQUAL tipo_de_dato TURBO_FISH NEW LPAREN RPAREN
                | LET ID DOUBLE_POINT tupla_asignacion EQUAL tupla_declaracion
                | LET ID EQUAL tupla_declaracion
                """

def p_tupla_asignacion(p):
  """tupla_asignacion : LPAREN tupla_lista_de_datos RPAREN
  """

def p_tupla_declaracion(p):
  """tupla_declaracion : LPAREN tupla_valores RPAREN"""

def p_tupla_lista_de_datos(p):
  """tupla_lista_de_datos : tipo_de_dato
                          | tipo_de_dato COMA tupla_lista_de_datos"""

def p_tupla_valores(p):
  """tupla_valores : valor
                    | valor COMA tupla_valores """

##FUNCIONES - HANS RAMOS
def p_definir_funcion(p):
  """definir_funcion : funcion_main 
                      | funcion"""

def p_funcion_main(p):
  """funcion_main : FN MAIN LPAREN RPAREN"""

def p_funcion(p):
  """funcion : FN ID LPAREN RPAREN
             | FN ID LPAREN lista_parametros RPAREN"""

def p_lista_parametros(p):
  """lista_parametros : ID DOUBLE_POINT tipo_de_dato
                      | ID DOUBLE_POINT tipo_de_dato COMA lista_parametros"""

##OPERACIONES - HANS RAMOS
def p_operaciones(p):
  """ operaciones : suma
                  | resta
                  | multiplicacion
                  | division
                  """

def p_suma(p):
  """suma : valor_numerico PLUS valor_numerico
          | suma PLUS valor_numerico """

def p_resta(p):
  """resta : valor_numerico MINUS valor_numerico
           | resta MINUS valor_numerico """

def p_multiplicacion(p):
  """multiplicacion : valor_numerico TIMES valor_numerico
                    | multiplicacion TIMES valor_numerico"""

def p_division(p):
  """division : valor_numerico DIVIDE valor_numerico"""

##COMPARACIONES -HANS RAMOS
def p_comparaciones(p):
  """comparaciones : menor
                   | menor_igual
                   | mayor
                   | mayor_igual
                   | igual"""

def p_menor(p):
  """menor : valor_numerico LESS valor_numerico"""
def p_menor_igual(p):
  """menor_igual : valor_numerico LESS EQUAL valor_numerico"""

def p_mayor(p):
  """mayor : valor_numerico GREAT valor_numerico"""
def p_mayor_igual(p):
  """mayor_igual : valor_numerico GREAT EQUAL valor_numerico"""

def p_igual(p):
  """igual : valor_numerico EQUAL EQUAL valor_numerico"""

##BNF PARA MANEJO DE DATOS - HANS RAMOS 
def p_tipo_de_dato(p):
  """tipo_de_dato : TIPO_STRING
                  | TIPO_BOOL
                  | TIPO_CHAR
                  | TIPO_INT"""

def p_valor(p):
  """valor  : valor_numerico
            | STRING
            | CHAR
            | BOOL"""

def p_valor_numerico(p):
  """valor_numerico : FLOAT
                    | NUMBER"""

##EXTRAS
def p_print(p):
  """print  : PRINTLN MACRO LPAREN valor RPAREN
            | PRINTLN LPAREN NUMBER RPAREN"""

def p_library_call(p):
  """library_call : USE library_path"""

def p_library_path(p):
  """library_path : ID 
                  | ID TURBO_FISH library_path"""

##MANEJADOR DE ERRORES 
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")

#BUILD THE PARSER 
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
