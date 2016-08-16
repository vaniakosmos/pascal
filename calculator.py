INTEGER, EOF = 'INTEGER', 'EOF'
PLUS, MINUS, MULTI, DIV = 'PLUS', 'MINUS', 'MULTI', 'DIV'


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return '<Token: {type}, {value}>'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

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

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            print(self.current_token)
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.current_token.value
        self.eat(INTEGER)

        while self.current_token.type is not EOF:
            op = self.current_token
            if op.type == PLUS:
                self.eat(PLUS)
            elif op.type == MINUS:
                self.eat(MINUS)
            elif op.type == MULTI:
                self.eat(MULTI)
            else:
                self.eat(DIV)

            right = self.current_token
            self.eat(INTEGER)

            if op.type == PLUS:
                result += right.value
            elif op.type == MINUS:
                result -= right.value
            elif op.type == MULTI:
                result *= right.value
            else:
                result /= right.value

        return result


def main():
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if not text or text == 'q':
            break
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
