
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS ASYN AWAY BOOL BREAK CHAR COMA CONST CONTINUE DIVIDE DOUBLE_POINT ELSE ENUM EQUAL FALSE FLOAT FN FOR FROM GREAT ID IF IN ITER LCORCH LESS LET LLLAV LPAREN MACRONOT MAIN MINUS MUT NEW NUMBER OR PLUS POP PRINTLN PUNTO PUNTO_COMA PUSH RCOM RCORCH RETURN RLLAV RPAREN STATIC STRING TIMES TIPO_BOOL TIPO_CHAR TIPO_INT TIPO_STRING TRUE TURBO_FISH USE VEC VEC_OBJ WHILEcuerpo : asignacion\n            | operaciones\n            | comparaciones\n            | definir_funcion\n            | llamada_a_metodo\n            | enum\n            | impresion\n            | library_callbooleano : TRUE\n                | FALSE\n    asignacion : declaracion ID DOUBLE_POINT VEC_OBJ LESS tipo_de_dato GREAT EQUAL VEC MACRONOT LCORCH tupla_valores RCORCH\n                | declaracion ID EQUAL VEC MACRONOT LCORCH tupla_valores RCORCH\n                | declaracion ID EQUAL VEC TURBO_FISH NEW LPAREN RPAREN\n                | declaracion ID EQUAL VEC MACRONOT LCORCH RCORCH\n                | declaracion ID EQUAL valor\n                | declaracion ID DOUBLE_POINT TIPO_INT EQUAL NUMBER\n                | declaracion ID DOUBLE_POINT TIPO_CHAR EQUAL CHAR\n                | declaracion ID DOUBLE_POINT TIPO_STRING EQUAL STRING\n                | declaracion ID EQUAL tipo_de_dato TURBO_FISH NEW LPAREN RPAREN\n                | declaracion DOUBLE_POINT tupla_asignacion EQUAL tupla_declaracion\n                | declaracion ID EQUAL tupla_declaracion\n                tupla_asignacion : LPAREN tupla_lista_de_datos RPAREN\n  declaracion : LET \n                 | LET MUT\n                 | CONSTtupla_declaracion : LPAREN tupla_valores RPARENtupla_lista_de_datos : tipo_de_dato\n                          | tipo_de_dato COMA tupla_lista_de_datostupla_valores : valor\n                    | valor COMA tupla_valores impresion : PRINTLN valor\n                  | PRINTLN MACRONOT valor\n                  | PRINTLN LPAREN valor RPAREN\n                  | PRINTLN MACRONOT LPAREN valor RPAREN\n    tipo_de_dato : TIPO_STRING\n                  | TIPO_BOOL\n                  | TIPO_CHAR\n                  | TIPO_INTvalor  : valor_numerico\n            | STRING\n            | CHAR\n            | BOOLvalor_numerico : FLOAT\n                    | NUMBER operaciones : suma\n                  | resta\n                  | multiplicacion\n                  | division\n                   suma : valor_numerico PLUS valor_numerico\n          | suma PLUS valor_numerico resta : valor_numerico MINUS valor_numerico\n           | resta MINUS valor_numerico multiplicacion : valor_numerico TIMES valor_numerico\n                    | multiplicacion TIMES valor_numericodivision : valor_numerico DIVIDE valor_numericooperacionArit : valor repite_operacionAritrepite_operacionArit : operaciones valor\n                              | operaciones valor repite_operacionArit\n    comparaciones : menor\n                   | menor_igual\n                   | mayor\n                   | mayor_igual\n                   | igualmenor : valor_numerico LESS valor_numericomenor_igual : valor_numerico LESS EQUAL valor_numericomayor : valor_numerico GREAT valor_numericomayor_igual : valor_numerico GREAT EQUAL valor_numericoigual : valor_numerico EQUAL EQUAL valor_numericooperacionComparacion : valor repite_operacionComparacionrepite_operacionComparacion : comparaciones valor\n                                   | comparaciones valor repite_operacionComparacion\n    definir_funcion : funcion_main \n                      | funcionfuncion_main : FN MAIN LPAREN RPARENfuncion : FN ID LPAREN RPAREN\n             | FN ID LPAREN lista_parametros RPARENlista_parametros : ID DOUBLE_POINT tipo_de_dato\n                      | ID DOUBLE_POINT tipo_de_dato COMA lista_parametrosllamada_a_metodo : ID PUNTO metodo\n                      | ID PUNTO NUMBERmetodo : pop_method\n            | push_methodpop_method : POP LPAREN RPAREN\n                | POP LPAREN NUMBER RPARENpush_method : PUSH LPAREN RPAREN\n                | PUSH LPAREN NUMBER RPARENenum : ENUM ID LLLAV lista_enum RLLAVlista_enum : lista_enum_id\n                | lista_enum_id_tipo\n                | lista_enum_tipolista_enum_id : ID\n                   | ID COMA lista_enum_idlista_enum_id_tipo : ID DOUBLE_POINT tipo_de_dato\n                         | ID DOUBLE_POINT tipo_de_dato lista_enum_id_tipolista_enum_tipo : tipo_de_dato\n                     | tipo_de_dato COMA lista_enum_tipooperadorLogico : AND\n                      | OR\n                      | MACRONOToperacionLogica : valor repite_operacionLogicarepite_operacionLogica : operadorLogico valor\n                              | operadorLogico valor repite_operacionLogicacondicion : booleano\n                 | operacionComparacion\n                 | operacionLogica\n    sentencias : IF LPAREN condicion RPAREN LLLAV cuerpo RLLAV\n                  | IF condicion RPAREN LLLAV cuerpo RLLAV\n                  | ELSE IF LPAREN condicion RPAREN  RPAREN LLLAV cuerpo RLLAV\n                  | ELSE IF condicion RPAREN LLLAV cuerpo RLLAV\n                  | ELSE RPAREN LLLAV cuerpo RLLAV\n    rango : NUMBER PUNTO PUNTO NUMBER\n          | NUMBER PUNTO PUNTO EQUAL NUMBER\n          | ID PUNTO ITER LPAREN RPAREN\n          | bucle : FOR ID IN rango LLLAV cuerpo RLLAVsentencias : WHILE condicion LLLAV cuerpo RLLAV\n               | WHILE LPAREN condicion RPAREN LLLAV cuerpo RLLAV\n    print  : PRINTLN MACRONOT LPAREN valor RPAREN\n            | PRINTLN LPAREN valor RPARENlibrary_call : USE library_pathlibrary_path : ID \n                  | ID TURBO_FISH library_pathoperacionAritNumeros : valor_numerico repite_operacionAritNumerosrepite_operacionAritNumeros : operaciones valor_numerico\n                              | operaciones valor_numerico repite_operacionAritNumeros\n    '
    
_lr_action_items = {'ID':([0,10,24,26,27,28,30,48,71,75,86,96,97,98,99,137,158,169,],[11,32,38,47,-23,-25,57,-24,105,47,118,-35,-36,-37,-38,156,167,118,]),'ENUM':([0,],[24,]),'PRINTLN':([0,],[25,]),'USE':([0,],[26,]),'LET':([0,],[27,]),'CONST':([0,],[28,]),'FN':([0,],[30,]),'FLOAT':([0,25,35,36,37,40,41,49,50,51,52,53,55,59,73,81,82,84,92,148,151,177,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'NUMBER':([0,25,34,35,36,37,40,41,49,50,51,52,53,55,59,73,81,82,84,92,103,104,122,148,151,177,],[12,12,63,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,134,136,145,12,12,12,]),'$end':([1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,20,21,22,23,31,39,42,43,44,45,46,47,62,63,64,65,68,69,70,72,76,77,78,79,80,83,93,95,112,113,114,115,116,117,119,130,133,135,139,141,143,145,146,147,150,154,155,163,171,172,173,179,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-44,-45,-46,-47,-48,-59,-60,-61,-62,-63,-72,-73,-43,-31,-39,-40,-41,-42,-120,-121,-79,-80,-81,-82,-50,-52,-54,-32,-49,-51,-53,-55,-64,-66,-15,-21,-33,-122,-65,-68,-67,-74,-75,-20,-83,-85,-87,-34,-76,-16,-17,-18,-26,-84,-86,-14,-12,-13,-19,-11,]),'DOUBLE_POINT':([10,27,28,32,48,105,118,167,],[33,-23,-25,58,-24,138,142,138,]),'PUNTO':([11,],[34,]),'PLUS':([12,13,29,31,68,76,],[-44,35,49,-43,-50,-49,]),'MINUS':([12,14,29,31,69,77,],[-44,36,50,-43,-52,-51,]),'TIMES':([12,15,29,31,70,78,],[-44,37,51,-43,-54,-53,]),'DIVIDE':([12,29,31,],[-44,52,-43,]),'LESS':([12,29,31,87,],[-44,53,-43,121,]),'GREAT':([12,29,31,96,97,98,99,144,],[-44,55,-43,-35,-36,-37,-38,161,]),'EQUAL':([12,29,31,32,53,54,55,60,88,89,90,131,161,],[-44,54,-43,59,81,82,84,100,122,123,124,-22,170,]),'RPAREN':([12,31,42,43,44,45,74,85,86,96,97,98,99,101,102,103,104,111,120,127,128,134,136,153,160,164,165,166,174,],[-44,-43,-39,-40,-41,-42,112,117,119,-35,-36,-37,-38,131,-27,133,135,141,143,150,-29,154,155,-28,-77,172,-30,173,-78,]),'COMA':([12,31,42,43,44,45,96,97,98,99,102,105,110,128,156,160,],[-44,-43,-39,-40,-41,-42,-35,-36,-37,-38,132,137,140,151,137,169,]),'RCORCH':([12,31,42,43,44,45,128,148,162,165,178,],[-44,-43,-39,-40,-41,-42,-29,163,171,-30,179,]),'MACRONOT':([25,91,175,],[40,125,176,]),'LPAREN':([25,33,40,56,57,59,66,67,100,149,152,],[41,61,73,85,86,92,103,104,92,164,166,]),'STRING':([25,40,41,59,73,92,124,148,151,177,],[43,43,43,43,43,43,147,43,43,43,]),'CHAR':([25,40,41,59,73,92,123,148,151,177,],[44,44,44,44,44,44,146,44,44,44,]),'BOOL':([25,40,41,59,73,92,148,151,177,],[45,45,45,45,45,45,45,45,45,]),'MUT':([27,],[48,]),'MAIN':([30,],[56,]),'POP':([34,],[66,]),'PUSH':([34,],[67,]),'LLLAV':([38,],[71,]),'TURBO_FISH':([47,91,94,96,97,98,99,],[75,126,129,-35,-36,-37,-38,]),'VEC_OBJ':([58,],[87,]),'TIPO_INT':([58,59,61,71,121,132,138,140,142,],[88,99,99,99,99,99,99,99,99,]),'TIPO_CHAR':([58,59,61,71,121,132,138,140,142,],[89,98,98,98,98,98,98,98,98,]),'TIPO_STRING':([58,59,61,71,121,132,138,140,142,],[90,96,96,96,96,96,96,96,96,]),'VEC':([59,170,],[91,175,]),'TIPO_BOOL':([59,61,71,121,132,138,140,142,],[97,97,97,97,97,97,97,97,]),'RLLAV':([96,97,98,99,105,106,107,108,109,110,156,157,158,159,168,],[-35,-36,-37,-38,-91,139,-88,-89,-90,-95,-91,-92,-93,-96,-94,]),'LCORCH':([125,176,],[148,177,]),'NEW':([126,129,],[149,152,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'cuerpo':([0,],[1,]),'asignacion':([0,],[2,]),'operaciones':([0,],[3,]),'comparaciones':([0,],[4,]),'definir_funcion':([0,],[5,]),'llamada_a_metodo':([0,],[6,]),'enum':([0,],[7,]),'impresion':([0,],[8,]),'library_call':([0,],[9,]),'declaracion':([0,],[10,]),'suma':([0,],[13,]),'resta':([0,],[14,]),'multiplicacion':([0,],[15,]),'division':([0,],[16,]),'menor':([0,],[17,]),'menor_igual':([0,],[18,]),'mayor':([0,],[19,]),'mayor_igual':([0,],[20,]),'igual':([0,],[21,]),'funcion_main':([0,],[22,]),'funcion':([0,],[23,]),'valor_numerico':([0,25,35,36,37,40,41,49,50,51,52,53,55,59,73,81,82,84,92,148,151,177,],[29,42,68,69,70,42,42,76,77,78,79,80,83,42,42,114,115,116,42,42,42,42,]),'valor':([25,40,41,59,73,92,148,151,177,],[39,72,74,93,111,128,128,128,128,]),'library_path':([26,75,],[46,113,]),'tupla_asignacion':([33,],[60,]),'metodo':([34,],[62,]),'pop_method':([34,],[64,]),'push_method':([34,],[65,]),'tipo_de_dato':([59,61,71,121,132,138,140,142,],[94,102,110,144,102,158,110,160,]),'tupla_declaracion':([59,100,],[95,130,]),'tupla_lista_de_datos':([61,132,],[101,153,]),'lista_enum':([71,],[106,]),'lista_enum_id':([71,137,],[107,157,]),'lista_enum_id_tipo':([71,158,],[108,168,]),'lista_enum_tipo':([71,140,],[109,159,]),'lista_parametros':([86,169,],[120,174,]),'tupla_valores':([92,148,151,177,],[127,162,165,178,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> cuerpo","S'",1,None,None,None),
  ('cuerpo -> asignacion','cuerpo',1,'p_cuerpo','sintactico.py',17),
  ('cuerpo -> operaciones','cuerpo',1,'p_cuerpo','sintactico.py',18),
  ('cuerpo -> comparaciones','cuerpo',1,'p_cuerpo','sintactico.py',19),
  ('cuerpo -> definir_funcion','cuerpo',1,'p_cuerpo','sintactico.py',20),
  ('cuerpo -> llamada_a_metodo','cuerpo',1,'p_cuerpo','sintactico.py',21),
  ('cuerpo -> enum','cuerpo',1,'p_cuerpo','sintactico.py',22),
  ('cuerpo -> impresion','cuerpo',1,'p_cuerpo','sintactico.py',23),
  ('cuerpo -> library_call','cuerpo',1,'p_cuerpo','sintactico.py',24),
  ('booleano -> TRUE','booleano',1,'p_booleano','sintactico.py',28),
  ('booleano -> FALSE','booleano',1,'p_booleano','sintactico.py',29),
  ('asignacion -> declaracion ID DOUBLE_POINT VEC_OBJ LESS tipo_de_dato GREAT EQUAL VEC MACRONOT LCORCH tupla_valores RCORCH','asignacion',13,'p_asignacion','sintactico.py',35),
  ('asignacion -> declaracion ID EQUAL VEC MACRONOT LCORCH tupla_valores RCORCH','asignacion',8,'p_asignacion','sintactico.py',36),
  ('asignacion -> declaracion ID EQUAL VEC TURBO_FISH NEW LPAREN RPAREN','asignacion',8,'p_asignacion','sintactico.py',37),
  ('asignacion -> declaracion ID EQUAL VEC MACRONOT LCORCH RCORCH','asignacion',7,'p_asignacion','sintactico.py',38),
  ('asignacion -> declaracion ID EQUAL valor','asignacion',4,'p_asignacion','sintactico.py',39),
  ('asignacion -> declaracion ID DOUBLE_POINT TIPO_INT EQUAL NUMBER','asignacion',6,'p_asignacion','sintactico.py',40),
  ('asignacion -> declaracion ID DOUBLE_POINT TIPO_CHAR EQUAL CHAR','asignacion',6,'p_asignacion','sintactico.py',41),
  ('asignacion -> declaracion ID DOUBLE_POINT TIPO_STRING EQUAL STRING','asignacion',6,'p_asignacion','sintactico.py',42),
  ('asignacion -> declaracion ID EQUAL tipo_de_dato TURBO_FISH NEW LPAREN RPAREN','asignacion',8,'p_asignacion','sintactico.py',43),
  ('asignacion -> declaracion DOUBLE_POINT tupla_asignacion EQUAL tupla_declaracion','asignacion',5,'p_asignacion','sintactico.py',44),
  ('asignacion -> declaracion ID EQUAL tupla_declaracion','asignacion',4,'p_asignacion','sintactico.py',45),
  ('tupla_asignacion -> LPAREN tupla_lista_de_datos RPAREN','tupla_asignacion',3,'p_tupla_asignacion','sintactico.py',49),
  ('declaracion -> LET','declaracion',1,'p_declaracion','sintactico.py',53),
  ('declaracion -> LET MUT','declaracion',2,'p_declaracion','sintactico.py',54),
  ('declaracion -> CONST','declaracion',1,'p_declaracion','sintactico.py',55),
  ('tupla_declaracion -> LPAREN tupla_valores RPAREN','tupla_declaracion',3,'p_tupla_declaracion','sintactico.py',57),
  ('tupla_lista_de_datos -> tipo_de_dato','tupla_lista_de_datos',1,'p_tupla_lista_de_datos','sintactico.py',60),
  ('tupla_lista_de_datos -> tipo_de_dato COMA tupla_lista_de_datos','tupla_lista_de_datos',3,'p_tupla_lista_de_datos','sintactico.py',61),
  ('tupla_valores -> valor','tupla_valores',1,'p_tupla_valores','sintactico.py',64),
  ('tupla_valores -> valor COMA tupla_valores','tupla_valores',3,'p_tupla_valores','sintactico.py',65),
  ('impresion -> PRINTLN valor','impresion',2,'p_impresion','sintactico.py',69),
  ('impresion -> PRINTLN MACRONOT valor','impresion',3,'p_impresion','sintactico.py',70),
  ('impresion -> PRINTLN LPAREN valor RPAREN','impresion',4,'p_impresion','sintactico.py',71),
  ('impresion -> PRINTLN MACRONOT LPAREN valor RPAREN','impresion',5,'p_impresion','sintactico.py',72),
  ('tipo_de_dato -> TIPO_STRING','tipo_de_dato',1,'p_tipo_de_dato','sintactico.py',77),
  ('tipo_de_dato -> TIPO_BOOL','tipo_de_dato',1,'p_tipo_de_dato','sintactico.py',78),
  ('tipo_de_dato -> TIPO_CHAR','tipo_de_dato',1,'p_tipo_de_dato','sintactico.py',79),
  ('tipo_de_dato -> TIPO_INT','tipo_de_dato',1,'p_tipo_de_dato','sintactico.py',80),
  ('valor -> valor_numerico','valor',1,'p_valor','sintactico.py',83),
  ('valor -> STRING','valor',1,'p_valor','sintactico.py',84),
  ('valor -> CHAR','valor',1,'p_valor','sintactico.py',85),
  ('valor -> BOOL','valor',1,'p_valor','sintactico.py',86),
  ('valor_numerico -> FLOAT','valor_numerico',1,'p_valor_numerico','sintactico.py',89),
  ('valor_numerico -> NUMBER','valor_numerico',1,'p_valor_numerico','sintactico.py',90),
  ('operaciones -> suma','operaciones',1,'p_operaciones','sintactico.py',95),
  ('operaciones -> resta','operaciones',1,'p_operaciones','sintactico.py',96),
  ('operaciones -> multiplicacion','operaciones',1,'p_operaciones','sintactico.py',97),
  ('operaciones -> division','operaciones',1,'p_operaciones','sintactico.py',98),
  ('suma -> valor_numerico PLUS valor_numerico','suma',3,'p_suma','sintactico.py',102),
  ('suma -> suma PLUS valor_numerico','suma',3,'p_suma','sintactico.py',103),
  ('resta -> valor_numerico MINUS valor_numerico','resta',3,'p_resta','sintactico.py',106),
  ('resta -> resta MINUS valor_numerico','resta',3,'p_resta','sintactico.py',107),
  ('multiplicacion -> valor_numerico TIMES valor_numerico','multiplicacion',3,'p_multiplicacion','sintactico.py',110),
  ('multiplicacion -> multiplicacion TIMES valor_numerico','multiplicacion',3,'p_multiplicacion','sintactico.py',111),
  ('division -> valor_numerico DIVIDE valor_numerico','division',3,'p_division','sintactico.py',114),
  ('operacionArit -> valor repite_operacionArit','operacionArit',2,'p_operacionArit','sintactico.py',118),
  ('repite_operacionArit -> operaciones valor','repite_operacionArit',2,'p_repite_operacionArit','sintactico.py',122),
  ('repite_operacionArit -> operaciones valor repite_operacionArit','repite_operacionArit',3,'p_repite_operacionArit','sintactico.py',123),
  ('comparaciones -> menor','comparaciones',1,'p_comparaciones','sintactico.py',129),
  ('comparaciones -> menor_igual','comparaciones',1,'p_comparaciones','sintactico.py',130),
  ('comparaciones -> mayor','comparaciones',1,'p_comparaciones','sintactico.py',131),
  ('comparaciones -> mayor_igual','comparaciones',1,'p_comparaciones','sintactico.py',132),
  ('comparaciones -> igual','comparaciones',1,'p_comparaciones','sintactico.py',133),
  ('menor -> valor_numerico LESS valor_numerico','menor',3,'p_menor','sintactico.py',136),
  ('menor_igual -> valor_numerico LESS EQUAL valor_numerico','menor_igual',4,'p_menor_igual','sintactico.py',138),
  ('mayor -> valor_numerico GREAT valor_numerico','mayor',3,'p_mayor','sintactico.py',141),
  ('mayor_igual -> valor_numerico GREAT EQUAL valor_numerico','mayor_igual',4,'p_mayor_igual','sintactico.py',143),
  ('igual -> valor_numerico EQUAL EQUAL valor_numerico','igual',4,'p_igual','sintactico.py',146),
  ('operacionComparacion -> valor repite_operacionComparacion','operacionComparacion',2,'p_operacionComparacion','sintactico.py',151),
  ('repite_operacionComparacion -> comparaciones valor','repite_operacionComparacion',2,'p_repite_operacionComparacion','sintactico.py',155),
  ('repite_operacionComparacion -> comparaciones valor repite_operacionComparacion','repite_operacionComparacion',3,'p_repite_operacionComparacion','sintactico.py',156),
  ('definir_funcion -> funcion_main','definir_funcion',1,'p_definir_funcion','sintactico.py',161),
  ('definir_funcion -> funcion','definir_funcion',1,'p_definir_funcion','sintactico.py',162),
  ('funcion_main -> FN MAIN LPAREN RPAREN','funcion_main',4,'p_funcion_main','sintactico.py',165),
  ('funcion -> FN ID LPAREN RPAREN','funcion',4,'p_funcion','sintactico.py',168),
  ('funcion -> FN ID LPAREN lista_parametros RPAREN','funcion',5,'p_funcion','sintactico.py',169),
  ('lista_parametros -> ID DOUBLE_POINT tipo_de_dato','lista_parametros',3,'p_lista_parametros','sintactico.py',172),
  ('lista_parametros -> ID DOUBLE_POINT tipo_de_dato COMA lista_parametros','lista_parametros',5,'p_lista_parametros','sintactico.py',173),
  ('llamada_a_metodo -> ID PUNTO metodo','llamada_a_metodo',3,'p_llamada_a_metodo','sintactico.py',178),
  ('llamada_a_metodo -> ID PUNTO NUMBER','llamada_a_metodo',3,'p_llamada_a_metodo','sintactico.py',179),
  ('metodo -> pop_method','metodo',1,'p_metodo','sintactico.py',182),
  ('metodo -> push_method','metodo',1,'p_metodo','sintactico.py',183),
  ('pop_method -> POP LPAREN RPAREN','pop_method',3,'p_pop_method','sintactico.py',186),
  ('pop_method -> POP LPAREN NUMBER RPAREN','pop_method',4,'p_pop_method','sintactico.py',187),
  ('push_method -> PUSH LPAREN RPAREN','push_method',3,'p_push_method','sintactico.py',190),
  ('push_method -> PUSH LPAREN NUMBER RPAREN','push_method',4,'p_push_method','sintactico.py',191),
  ('enum -> ENUM ID LLLAV lista_enum RLLAV','enum',5,'p_enum','sintactico.py',195),
  ('lista_enum -> lista_enum_id','lista_enum',1,'p_lista_enum','sintactico.py',198),
  ('lista_enum -> lista_enum_id_tipo','lista_enum',1,'p_lista_enum','sintactico.py',199),
  ('lista_enum -> lista_enum_tipo','lista_enum',1,'p_lista_enum','sintactico.py',200),
  ('lista_enum_id -> ID','lista_enum_id',1,'p_lista_enum_id','sintactico.py',203),
  ('lista_enum_id -> ID COMA lista_enum_id','lista_enum_id',3,'p_lista_enum_id','sintactico.py',204),
  ('lista_enum_id_tipo -> ID DOUBLE_POINT tipo_de_dato','lista_enum_id_tipo',3,'p_lista_enum_id_tipo','sintactico.py',207),
  ('lista_enum_id_tipo -> ID DOUBLE_POINT tipo_de_dato lista_enum_id_tipo','lista_enum_id_tipo',4,'p_lista_enum_id_tipo','sintactico.py',208),
  ('lista_enum_tipo -> tipo_de_dato','lista_enum_tipo',1,'p_lista_enum_tipo','sintactico.py',211),
  ('lista_enum_tipo -> tipo_de_dato COMA lista_enum_tipo','lista_enum_tipo',3,'p_lista_enum_tipo','sintactico.py',212),
  ('operadorLogico -> AND','operadorLogico',1,'p_operadorLogico','sintactico.py',217),
  ('operadorLogico -> OR','operadorLogico',1,'p_operadorLogico','sintactico.py',218),
  ('operadorLogico -> MACRONOT','operadorLogico',1,'p_operadorLogico','sintactico.py',219),
  ('operacionLogica -> valor repite_operacionLogica','operacionLogica',2,'p_operacionLogica','sintactico.py',222),
  ('repite_operacionLogica -> operadorLogico valor','repite_operacionLogica',2,'p_repite_operacionLogica','sintactico.py',226),
  ('repite_operacionLogica -> operadorLogico valor repite_operacionLogica','repite_operacionLogica',3,'p_repite_operacionLogica','sintactico.py',227),
  ('condicion -> booleano','condicion',1,'p_condicion','sintactico.py',236),
  ('condicion -> operacionComparacion','condicion',1,'p_condicion','sintactico.py',237),
  ('condicion -> operacionLogica','condicion',1,'p_condicion','sintactico.py',238),
  ('sentencias -> IF LPAREN condicion RPAREN LLLAV cuerpo RLLAV','sentencias',7,'p_bucle_condicional','sintactico.py',241),
  ('sentencias -> IF condicion RPAREN LLLAV cuerpo RLLAV','sentencias',6,'p_bucle_condicional','sintactico.py',242),
  ('sentencias -> ELSE IF LPAREN condicion RPAREN RPAREN LLLAV cuerpo RLLAV','sentencias',9,'p_bucle_condicional','sintactico.py',243),
  ('sentencias -> ELSE IF condicion RPAREN LLLAV cuerpo RLLAV','sentencias',7,'p_bucle_condicional','sintactico.py',244),
  ('sentencias -> ELSE RPAREN LLLAV cuerpo RLLAV','sentencias',5,'p_bucle_condicional','sintactico.py',245),
  ('rango -> NUMBER PUNTO PUNTO NUMBER','rango',4,'p_rangoSentencia','sintactico.py',252),
  ('rango -> NUMBER PUNTO PUNTO EQUAL NUMBER','rango',5,'p_rangoSentencia','sintactico.py',253),
  ('rango -> ID PUNTO ITER LPAREN RPAREN','rango',5,'p_rangoSentencia','sintactico.py',254),
  ('rango -> <empty>','rango',0,'p_rangoSentencia','sintactico.py',255),
  ('bucle -> FOR ID IN rango LLLAV cuerpo RLLAV','bucle',7,'p_bucle_for','sintactico.py',258),
  ('sentencias -> WHILE condicion LLLAV cuerpo RLLAV','sentencias',5,'p_bucle_while','sintactico.py',264),
  ('sentencias -> WHILE LPAREN condicion RPAREN LLLAV cuerpo RLLAV','sentencias',7,'p_bucle_while','sintactico.py',265),
  ('print -> PRINTLN MACRONOT LPAREN valor RPAREN','print',5,'p_print','sintactico.py',271),
  ('print -> PRINTLN LPAREN valor RPAREN','print',4,'p_print','sintactico.py',272),
  ('library_call -> USE library_path','library_call',2,'p_library_call','sintactico.py',275),
  ('library_path -> ID','library_path',1,'p_library_path','sintactico.py',278),
  ('library_path -> ID TURBO_FISH library_path','library_path',3,'p_library_path','sintactico.py',279),
  ('operacionAritNumeros -> valor_numerico repite_operacionAritNumeros','operacionAritNumeros',2,'p_operacionAritNumeros','sintactico.py',285),
  ('repite_operacionAritNumeros -> operaciones valor_numerico','repite_operacionAritNumeros',2,'p_repite_operacionAritNumeros','sintactico.py',288),
  ('repite_operacionAritNumeros -> operaciones valor_numerico repite_operacionAritNumeros','repite_operacionAritNumeros',3,'p_repite_operacionAritNumeros','sintactico.py',289),
]
