from calc.token import Token

INTEGER, EOF = 'INTEGER', 'EOF'
PLUS, MINUS, MULTI, DIV = 'PLUS', 'MINUS', 'MULTI', 'DIV'


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    ##########################################################
    #                       Lexer code                       #
    ##########################################################
    @staticmethod
    def error():
        raise Exception('Error parsing input')

    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Lexical analyzer

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULTI, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)

    ##########################################################
    #               Parser / Interpreter code                #
    ##########################################################
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            # print(self.current_token)
        else:
            self.error()

    def term(self):
        """Return an INTEGER token value"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        while self.current_token.type in (MULTI, DIV):
            token = self.current_token
            if token.type == MULTI:
                self.eat(MULTI)
                result = result * self.term()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.term()

        return result
