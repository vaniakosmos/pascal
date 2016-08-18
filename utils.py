from token import Token

INTEGER, EOF = 'INTEGER', 'EOF'
PLUS, MINUS, MUL, DIV = 'PLUS', 'MINUS', 'MUL', 'DIV'
LPAREN, RPAREN = '(', ')'
ASSIGN, SEMI, DOT = ':=', ';', 'DOT'
BEGIN, END, ID = 'BEGIN', 'END', 'ID'

OPERATIONS = (PLUS, MINUS, MUL, DIV)

RESERVED_KEYWORDS = {
        'BEGIN': Token('BEGIN', 'BEGIN'),
        'END': Token('END', 'END'),
    }
