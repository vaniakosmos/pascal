from lexer import Lexer

from ast import Interpreter
from ast import Parser


def main():
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if not text or text == 'q':
            break
        calc_lexer = Lexer(text)
        parser = Parser(calc_lexer)
        calc_interpreter = Interpreter(parser)
        result = calc_interpreter.interpret()
        print(result)


if __name__ == '__main__':
    main()
