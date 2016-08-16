from calc.utils import *


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    @staticmethod
    def error():
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        """Return an INTEGER token value"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        self.current_token = self.lexer.get_next_token()

        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.term()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.term()

        return result
