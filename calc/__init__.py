from calc.interpreter import Interpreter
from calc.lexer import Lexer


def main():
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if not text or text == 'q':
            break
        calc_lexer = Lexer(text)
        calc_interpreter = Interpreter(calc_lexer)
        result = calc_interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
