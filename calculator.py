from re import sub

INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


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
        self.text = sub(' ', '', text)
        self.pos = 0
        self.current_token = None

    @staticmethod
    def error():
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, valid_token_types):
        if self.current_token.type in valid_token_types:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def get_big_int(self):
        big_int = 0
        while self.current_token.type == INTEGER:
            left = self.current_token
            self.eat([INTEGER])
            big_int = big_int * 10 + left.value
        return big_int

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.get_big_int()

        op = self.current_token
        self.eat([PLUS, MINUS])

        right = self.get_big_int()

        if op.type == PLUS:
            result = left + right
        else:
            result = left - right
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
