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

    @staticmethod
    def read_rpn(notation):
        stack = []
        for token in notation:
            if token not in OPERATIONS:
                stack.append(token)
            else:
                y = stack.pop(-1)
                x = stack.pop(-1)
                if token == PLUS:
                    stack.append(x + y)

                elif token == MINUS:
                    stack.append(x - y)

                elif token == MUL:
                    stack.append(x * y)

                elif token == DIV:
                    stack.append(x // y)

                else:
                    Interpreter.error()
                # print('{} {} {} = {}'.format(x, token, y, stack[-1]))
        return stack[0]

    def expr(self):
        self.current_token = self.lexer.get_next_token()

        notation = []
        ops = []

        last_high = False
        while self.current_token.type != EOF:
            token = self.current_token

            if token.type == INTEGER:
                if last_high:
                    notation[-1][-2] = token.value
                else:
                    notation.append([token.value])

            elif token.type in (MUL, DIV):
                last_high = True
                notation[-1].append(None)
                notation[-1].append(token.type)

            elif token.type in (PLUS, MINUS):
                last_high = False
                ops.append(token.type)

            else:
                self.error()

            self.current_token = self.lexer.get_next_token()

        res = notation[0]
        i = 0
        for note in notation[1:]:
            res += note + [ops[i]]
            i += 1

        return self.read_rpn(res)

if __name__ == '__main__':
    print(Interpreter.read_rpn([14, 2, 3, 'MUL', 'PLUS', 6, 2, 'DIV', 'MINUS']))
