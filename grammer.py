Rull_List = []

NON_TERMINALS = ['Goal', 'Source', 'MainClass', 'ClassDeclarations', 'ClassDeclaration', 'Extension', 'FieldDeclarations',
             'FieldDeclaration', 'VarDeclarations', 'VarDeclaration', 'MethodDeclarations', 'MethodDeclaration', 'Parameters',
             'Parameter', 'Type', 'Statements', 'Statement', 'A', 'GenExpression', 'G', 'Expression', 'BB',
             'B', 'Term', 'C', 'Factor', 'D', 'RelExpression', 'E', 'RelTerm', 'F', 'Arguments', 'Argument',
             'Identifier', 'Integer', 'DD']
TERMINALS = ['EOF', 'public', 'class', 'static', 'void', 'main', '{', '}', '(', ')', ';', '=', '==', '+', '-',
             'extends', 'return', ',', 'boolean', 'int', 'if', 'for', 'while', 'System.out.println', '*', 'true',
             'false', '&&', 'identifier', 'integer', 'else', '.', '+=', '<']

GRAMMAR = {
    1: "Goal Source EOF",
    2: "Source ClassDeclarations MainClass",
    3: "MainClass public class @identifier_class @set_local_search Identifier @remove_last @start_scope @reset_local_search { public static void main ( ) { VarDeclarations Statements } @end_scope }",
    4: "ClassDeclarations ClassDeclaration ClassDeclarations",
    5: "ClassDeclarations",
    6: "ClassDeclaration class @identifier_class @set_local_search Identifier @remove_last @start_scope @reset_local_search Extension { FieldDeclarations MethodDeclarations @end_scope }",
    7: "Extension extends @create_extend Identifier @remove_last",
    8: "Extension",
    9: "FieldDeclarations FieldDeclaration FieldDeclarations",
    10: "FieldDeclarations",
    11: "FieldDeclaration static Type @set_local_search Identifier @remove_last @reset_local_search ;",
    12: "VarDeclarations VarDeclaration VarDeclarations",
    13: "VarDeclarations",
    14: "VarDeclaration Type @set_local_search Identifier @remove_last @reset_local_search ;",
    15: "MethodDeclarations MethodDeclaration MethodDeclarations",
    16: "MethodDeclarations",
    17: "MethodDeclaration public static Type @set_local_search @identifier_method Identifier @add_row @start_scope @reset_local_search ( Parameters ) #get_current_line @end_parameter { VarDeclarations Statements return GenExpression #return_assign ; @end_scope }",
    18: "Parameters Type @set_local_search Identifier @identifier_parameter Parameter @reset_local_search",
    19: "Parameters",
    20: "Parameter , Type Identifier @identifier_parameter Parameter",
    21: "Parameter",
    22: "Type boolean @identifier_boolean",
    23: "Type int @identifier_int",
    24: "Statements A",
    25: "A Statement A",
    26: "A",
    27: "Statement { Statements }",
    28: "Statement if ( GenExpression ) #save Statement else #jpf_save Statement #jump_here",
    29: "Statement while ( #label GenExpression #save ) Statement #end_while",
    30: "Statement for ( Identifier = Integer #assign ; #label RelTerm #save ; Identifier += Integer #plus_assign ) Statement #end_for",
    31: "Statement Identifier = GenExpression #assign ;",
    32: "Statement System.out.println ( GenExpression ) #sys_out ;",
    33: "GenExpression Expression G",
    34: "G F E",
    35: "Expression Term BB",
    36: "BB B BB",
    37: "BB",
    38: "B + Term #plus_operation",
    39: "B - Term #minus_operation",
    40: "Term Factor C",
    41: "C * Factor #multi_operation C",
    42: "C",
    43: "Factor ( Expression )",
    44: "Factor Identifier #identifier_name D",
    45: "Factor true #immediate_bool",
    46: "Factor false #immediate_bool",
    47: "Factor Integer",
    48: "D @remove_last",
    49: "D @set_search_scope . Identifier @reset_search_scope DD",
    50: "DD",
    51: "DD ( Arguments ) #call_method",  # TODO: support this!
    52: "RelExpression RelTerm E",
    53: "E",
    54: "E && RelTerm #and_operation E",
    55: "RelTerm Expression F",
    56: "F == Expression #rel_equal",
    57: "F < Expression #rel_less",
    58: "Arguments @add_zero GenExpression @save_argument Argument",
    59: "Arguments",
    60: "Argument , GenExpression @save_argument Argument",
    61: "Argument",
    62: "Identifier identifier @identifier #identifier",
    63: "Integer integer #immediate_integer",
    64: "G"
}

PARSER_TABLE = {
    "Goal": {"class": 1, "public": 1},
    "Source": {"class": 2, "public": 2},
    "MainClass": {"public": 3},
    "ClassDeclarations": {"public": 5, "class": 4},
    "ClassDeclaration": {"class": 6},
    "Extension": {"extends": 7, "{": 8},
    "FieldDeclarations": {"public": 10, "}": 10, "static": 9},
    "FieldDeclaration": {"static": 11},
    "VarDeclarations": {'{': 13, 'if': 13, 'while': 13, 'for': 13, 'identifier': 13, 'System.out.println': 13, '}': 13, 'return': 13, "boolean": 12, "int": 12},
    "VarDeclaration": {"boolean": 14, "int": 14},
    "MethodDeclarations": {"}": 16, "public": 15},
    "MethodDeclaration": {"public": 17},
    "Parameters": {"boolean": 18, "int": 18, ")": 19},
    "Parameter": {",": 20, ")": 21},
    "Type": {"boolean": 22, "int": 23},
    "Statements": {"{": 24, "if": 24, "while": 24, "for": 24, "identifier": 24, "System.out.println": 24, "}": 24, "return": 24},
    "Statement": {"{": 27, "if": 28, "while": 29, "for": 30, "identifier": 31, "System.out.println": 32},
    "GenExpression": {'(': 33, 'identifier': 33, 'true': 33, 'false': 33, 'integer': 33},
    "Expression": {'(': 35, 'identifier': 35, 'true': 35, 'false': 35, 'integer': 35},
    "Term": {"(": 40, "true": 40, "false": 40, "identifier": 40, "integer": 40},
    "Factor": {"(": 43, "true": 45, "false": 46, "identifier": 44, "integer": 47},
    "RelExpression": {'(': 52, 'identifier': 52, 'true': 52, 'false': 52, 'integer': 52},
    "RelTerm": {'(': 55, 'identifier': 55, 'true': 55, 'false': 55, 'integer': 55},
    "Arguments": {'(': 58, 'identifier': 58, 'true': 58, 'false': 58, 'integer': 58, ')': 59},
    "Argument": {",": 60, ")": 61},
    "Identifier": {"identifier": 62},
    "Integer": {"integer": 63},
    "A": {"{": 25, "if": 25, "while": 25, "for": 25, "identifier": 25, "System.out.println": 25, "}": 26, "return": 26},
    "B": {"+": 38, "-": 39},
    "BB": {"+": 36, "-": 36, '&&': 37, '<': 37, '==': 37, ')': 37, ';': 37, ',': 37},
    "C": {"*": 41, '+': 42, '-': 42, '&&': 42, '<': 42, '==': 42, ')': 42, ';': 42, ',': 42},
    "D": {".": 49, '+': 48, '-': 48, '&&': 48, '<': 48, '==': 48, ')': 48, ';': 48, ',': 48, '*': 48},
    "DD": {'+': 50, '-': 50, '&&': 50, '<': 50, '==': 50, ')': 50, ';': 50, ',': 50, '*': 50, "(": 51},
    "E": {';': 53, ')': 53, ',': 53, "&&": 54},
    "F": {"==": 56, "<": 57},
    "G": {'&&': 34, '<': 34, '==': 34, ';': 64, ')': 64, ',': 64}
}


FIRST = {'Goal': ['public', 'class'],
         'Source': ['public', 'class'],
         'MainClass': ['public'],
         'ClassDeclarations': ['class', ' '],
         'ClassDeclaration': ['class'],
         'Extension': ['extends', ' '],
         'FieldDeclarations': [' ', 'static'],
         'FieldDeclaration': ['static'],
         'VarDeclarations': ['int', 'boolean', ' '],
         'VarDeclaration': ['int', 'boolean'],
         'MethodDeclarations': ['public', ' '],
         'MethodDeclaration': ['public'],
         'Parameters': ['boolean', 'int', ' '],
         'Parameter': [',', ' '],
         'Type': ['boolean', 'int'],
         'Statements': ['{', 'if', 'while', 'for', 'identifier', 'System.out.println', ' '],
         'Statement': ['{', 'if', 'while', 'for', 'identifier', 'System.out.println'],
         'A': ['{', 'if', 'while', 'for', 'identifier', 'System.out.println', ' '],
         'GenExpression': ['(', 'identifier', 'true', 'false', 'integer'],
         'G': ['&&', '<', '==', ' '],
         'Expression': ['(', 'identifier', 'true', 'false', 'integer'],
         'BB': ['+', '-', ' '],
         'B': ['+', '-'],
         'Term': ['(', 'identifier', 'true', 'false', 'integer'],
         'C': ['*', ' '],
         'Factor': ['(', 'identifier', 'true', 'false', 'integer'],
         'D': ['.', ' '],
         'RelExpression': ['(', 'identifier', 'true', 'false', 'integer'],
         'E': ['&&', ' '],
         'RelTerm': ['(', 'identifier', 'true', 'false', 'integer'],
         'F': ['==', '<'],
         'Arguments': ['(', 'identifier', 'true', 'false', 'integer', ' '],
         'Argument': [',', ' '],
         'Identifier': ['identifier'],
         'Integer': ['integer'],
         'DD': ['(', ' ']
}

FOLLOW = {'Goal': [''],
          'Source': ['EOF'],
          'MainClass': ['EOF'],
          'ClassDeclarations': ['public'],
          'ClassDeclaration': ['class', 'public'],
          'Extension': ['{'],
          'FieldDeclarations': ['public', '}'],
          'FieldDeclaration': ['static', 'public', '}'],
          'VarDeclarations': ['{', 'if', 'while', 'for', 'identifier', 'System.out.println', '}', 'return'],
          'VarDeclaration': ['int', 'boolean', '{', 'if', 'while', 'for', 'identifier', 'System.out.println', '}', 'return'],
          'MethodDeclarations': ['}'],
          'MethodDeclaration': ['public', '}'],
          'Parameters': [')'],
          'Parameter': [')'],
          'Type': ['identifier'],
          'Statements': ['return', '}'],
          'Statement': ['{', 'if', 'while', 'for', 'identifier', 'System.out.println', 'return', 'else', '}'],
          'A': ['return', '}'],
          'GenExpression': [';', ')', ','],
          'G': [';', ')', ','],
          'Expression': ['&&', '<', '==', ')', ';', ','],
          'BB': ['&&', '<', '==', ')', ';', ','],
          'B': ['+', '-', '&&', '<', '==', ')', ';', ','],
          'Term': ['+', '-', '&&', '<', '==', ')', ';', ','],
          'C': ['+', '-', '&&', '<', '==', ')', ';', ','],
          'Factor': ['+', '-', '&&', '<', '==', ')', ';', ',', '*'],
          'D': ['+', '-', '&&', '<', '==', ')', ';', ',', '*'],
          'RelExpression': [],
          'E': [';', ')', ','],
          'RelTerm': [';', '&&', '==', '<'],
          'F': [';', '&&', '==', '<', ')', ','],
          'Arguments': [')'],
          'Argument': [')'],
          'DD': ['+', '-', '&&', '<', '==', ')', ';', ',', '*'],
          'Identifier': ['{', 'extends', ';', '(', ',', ')', '}', 'return', '=', '+=', '.', '==', '*', '<', '+', '-', '&&'],
          'Integer': [';', ')', '+', '-', '&&', '<', '==', ')', ';', '*']
}
