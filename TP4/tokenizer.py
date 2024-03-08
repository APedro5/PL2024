import ply.lex as lex

# Lista de tokens
tokens = (
    'SELECT', 'FROM', 'WHERE', 'ORDER', 'BY', 'GROUP', 'HAVING',
    'INSERT', 'INTO', 'VALUES',
    'UPDATE', 'SET',
    'DELETE',
    'CREATE', 'TABLE', 'INDEX', 'PRIMARY', 'KEY', 'UNIQUE',
    'ALTER', 'ADD', 'DROP',
    'AND', 'OR', 'NOT',
    'IDENTIFIER', 'NUMBER', 'STRING',
    'COMMA', 'DOT', 'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE',
    'LPAREN', 'RPAREN',
)

t_COMMA = r','
t_DOT = r'\.'
t_EQ = r'='
t_NEQ = r'!='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_SELECT(t):
    r'[Ss][Ee][Ll][Ee][Cc][Tt]'
    return t

def t_FROM(t):
    r'[Ff][Rr][Oo][Mm]'
    return t

def t_WHERE(t):
    r'[Ww][Hh][Ee][Rr][Ee]'
    return t

def t_ORDER(t):
    r'[Oo][Rr][Dd][Ee][Rr]'
    return t

def t_BY(t):
    r'[Bb][Yy]'
    return t

def t_GROUP(t):
    r'[Gg][Rr][Oo][Uu][Pp]'
    return t

def t_HAVING(t):
    r'[Hh][Aa][Vv][Ii][Nn][Gg]'
    return t

def t_INSERT(t):
    r'[Ii][Nn][Ss][Ee][Rr][Tt]'
    return t

def t_INTO(t):
    r'[Ii][Nn][Tt][Oo]'
    return t

def t_VALUES(t):
    r'[Vv][Aa][Ll][Uu][Ee][Ss]'
    return t

def t_UPDATE(t):
    r'[Uu][Pp][Dd][Aa][Tt][Ee]'
    return t

def t_SET(t):
    r'[Ss][Ee][Tt]'
    return t

def t_DELETE(t):
    r'[Dd][Ee][Ll][Ee][Tt][Ee]'
    return t

def t_CREATE(t):
    r'[Cc][Rr][Ee][Aa][Tt][Ee]'
    return t

def t_TABLE(t):
    r'[Tt][Aa][Bb][Ll][Ee]'
    return t

def t_INDEX(t):
    r'[Ii][Nn][Dd][Ee][Xx]'
    return t

def t_PRIMARY(t):
    r'[Pp][Rr][Ii][Mm][Aa][Rr][Yy]'
    return t

def t_KEY(t):
    r'[Kk][Ee][Yy]'
    return t

def t_UNIQUE(t):
    r'[Uu][Nn][Ii][Qq][Uu][Ee]'
    return t

def t_ALTER(t):
    r'[Aa][Ll][Tt][Ee][Rr]'
    return t

def t_ADD(t):
    r'[Aa][Dd][Dd]'
    return t

def t_DROP(t):
    r'[Dd][Rr][Oo][Pp]'
    return t

def t_AND(t):
    r'[Aa][Nn][Dd]'
    return t

def t_OR(t):
    r'[Oo][Rr]'
    return t

def t_NOT(t):
    r'[Nn][Oo][Tt]'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\'[^\']*\'|\"[^\"]*\"'
    t.value = t.value[1:-1]  # Remover as aspas
    return t

# Ignorar espaços em branco e tabs
t_ignore = ' \t'

# Lidar com quebras de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratar erros
def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Criar o analisador léxico
analexer = lex.lex()

