from lexer import Lexer
from interpreter import Interpreter
from parser import Parser


def main():
    text = ' '.join(open('test.txt'))
    t_lexer = Lexer(text)
    t_parser = Parser(t_lexer)
    t_interpreter = Interpreter(t_parser)
    t_interpreter.interpret()
    print(t_interpreter.GLOBAL_SCOPE)


if __name__ == '__main__':
    main()
