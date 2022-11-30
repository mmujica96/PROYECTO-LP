import ply.yacc as yacc
from lexico import tokens
import logging


logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()



def p_cuerpo(p):
  """cuerpo : asignacion
            | operaciones
            | comparaciones
            | definir_funcion
            | llamada_a_metodo
            | enum
            | impresion
            | library_call"""


def p_booleano(p):
    '''booleano : TRUE
                | FALSE
    '''

##ASIGNACION - HANS RAMOS

def p_asignacion(p):
  """asignacion : declaracion ID DOUBLE_POINT VEC_OBJ LESS tipo_de_dato GREAT EQUAL VEC MACRONOT LCORCH tupla_valores RCORCH
                | declaracion ID EQUAL VEC MACRONOT LCORCH tupla_valores RCORCH
                | declaracion ID EQUAL VEC TURBO_FISH NEW LPAREN RPAREN
                | declaracion ID EQUAL VEC MACRONOT LCORCH RCORCH
                | declaracion ID EQUAL valor
                | declaracion ID DOUBLE_POINT TIPO_INT EQUAL NUMBER
                | declaracion ID DOUBLE_POINT TIPO_CHAR EQUAL CHAR
                | declaracion ID DOUBLE_POINT TIPO_STRING EQUAL STRING
                | declaracion ID EQUAL tipo_de_dato TURBO_FISH NEW LPAREN RPAREN
                | declaracion DOUBLE_POINT tupla_asignacion EQUAL tupla_declaracion
                | declaracion ID EQUAL tupla_declaracion
                """

def p_tupla_asignacion(p):
  """tupla_asignacion : LPAREN tupla_lista_de_datos RPAREN
  """

def p_declaracion(p):
  """declaracion : LET 
                 | LET MUT
                 | CONST"""
def p_tupla_declaracion(p):
  """tupla_declaracion : LPAREN tupla_valores RPAREN"""

def p_tupla_lista_de_datos(p):
  """tupla_lista_de_datos : tipo_de_dato
                          | tipo_de_dato COMA tupla_lista_de_datos"""

def p_tupla_valores(p):
  """tupla_valores : valor
                    | valor COMA tupla_valores """

                    
def p_impresion(p):
    '''impresion : PRINTLN valor
                  | PRINTLN MACRONOT valor
                  | PRINTLN LPAREN valor RPAREN
                  | PRINTLN MACRONOT LPAREN valor RPAREN
    '''

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

##admiten mas de una operacion - MICHELLE MUJICA
def p_operacionArit(p):
    'operacionArit : valor repite_operacionArit'


def p_repite_operacionArit(p):
    '''repite_operacionArit : operaciones valor
                              | operaciones valor repite_operacionArit
    '''


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

##admiten mas de una operacion - MICHELLE MUJICA

def p_operacionComparacion(p):
    'operacionComparacion : valor repite_operacionComparacion'


def p_repite_operacionComparacion(p):
    '''repite_operacionComparacion : comparaciones valor
                                   | comparaciones valor repite_operacionComparacion
    '''

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

##LLAMADA A METODOS - HANS RAMOS

def p_llamada_a_metodo(p):
  """llamada_a_metodo : ID PUNTO metodo
                      | ID PUNTO NUMBER"""

def p_metodo(p):
  """metodo : pop_method
            | push_method"""

def p_pop_method(p):
  """pop_method : POP LPAREN RPAREN
                | POP LPAREN NUMBER RPAREN"""

def p_push_method(p):
  """push_method : PUSH LPAREN RPAREN
                | PUSH LPAREN NUMBER RPAREN"""

##ENUM - HANS RAMOS
def p_enum(p):
  """enum : ENUM ID LLLAV lista_enum RLLAV"""

def p_lista_enum(p):
  """lista_enum : lista_enum_id
                | lista_enum_id_tipo
                | lista_enum_tipo"""

def p_lista_enum_id(p):
  """lista_enum_id : ID
                   | ID COMA lista_enum_id"""

def p_lista_enum_id_tipo(p):
  """lista_enum_id_tipo : ID DOUBLE_POINT tipo_de_dato
                         | ID DOUBLE_POINT tipo_de_dato lista_enum_id_tipo"""

def p_lista_enum_tipo(p):
  """lista_enum_tipo : tipo_de_dato
                     | tipo_de_dato COMA lista_enum_tipo"""


# Operaciones logicas -- Michelle Mujica
def p_operadorLogico(p):
    """operadorLogico : AND
                      | OR
                      | MACRONOT"""

def p_operacionLogica(p):
    'operacionLogica : valor repite_operacionLogica'


def p_repite_operacionLogica(p):
    """repite_operacionLogica : operadorLogico valor
                              | operadorLogico valor repite_operacionLogica"""



#Estructuras de Control -- Michelle Mujica

#Bucle if

def p_condicion(p):
    '''condicion : booleano
                 | operacionComparacion
                 | operacionLogica
    '''
def p_bucle_condicional(p):
    '''sentencias : IF LPAREN condicion RPAREN LLLAV cuerpo RLLAV
                  | IF condicion RPAREN LLLAV cuerpo RLLAV
                  | ELSE IF LPAREN condicion RPAREN  RPAREN LLLAV cuerpo RLLAV
                  | ELSE IF condicion RPAREN LLLAV cuerpo RLLAV
                  | ELSE RPAREN LLLAV cuerpo RLLAV
    '''


# Bucle for

def p_rangoSentencia(p):
  """rango : NUMBER PUNTO PUNTO NUMBER
          | NUMBER PUNTO PUNTO EQUAL NUMBER
          | ID PUNTO ITER LPAREN RPAREN
          | """

def p_bucle_for(p):
    'bucle : FOR ID IN rango LLLAV cuerpo RLLAV'


#Bucle while

def p_bucle_while(p):
    '''sentencias : WHILE condicion LLLAV cuerpo RLLAV
               | WHILE LPAREN condicion RPAREN LLLAV cuerpo RLLAV
    '''


##EXTRAS
def p_print(p):
  """print  : PRINTLN MACRONOT LPAREN valor RPAREN
            | PRINTLN LPAREN valor RPAREN"""

def p_library_call(p):
  """library_call : USE library_path"""

def p_library_path(p):
  """library_path : ID 
                  | ID TURBO_FISH library_path"""


## ********************SEMANTICAS ***************
#MICHELLE MUJICA
def p_operacionAritNumeros(p):
  'operacionAritNumeros : valor_numerico repite_operacionAritNumeros'

def p_repite_operacionAritNumeros(p):
    '''repite_operacionAritNumeros : operaciones valor_numerico
                              | operaciones valor_numerico repite_operacionAritNumeros
    '''

##MANEJADOR DE ERRORES 
def p_error(p):
  if p:
    resultado = "Error Sintactico del token de tipo: {} , en el valor: {}".format(
      str(p.type), str(p.value))
    print(resultado)
  else:
    resultado = "Error de sintaxis: {}".format(p)
    print(resultado)
    

entradaGUI = []

#BUILD THE PARSER 
parser = yacc.yacc(debug=True,debuglog=log)

def leerAlgoritmoSintactico(entrada):
  entradaGUI.clear()
  lineas = entrada.split("\n")
  for line in lineas:
    if line != "\n":
      if line[:3] == "for" or line[:3] == "def" or line[:5] == "while" or line[:2] == "if":
                nLine = line.replace("\n", "")
                for Eline in entrada:
                    nLine += " " + Eline.replace("\n", "").replace("\t", "")
                    if Eline[:3] == "end":
                        break
                line = nLine
      entradaGUI.append(line)
      parser.parse(line)
    return entradaGUI

