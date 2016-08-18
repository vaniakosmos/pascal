from lexer import Lexer
from interpreter import Interpreter
from parser import Parser


def main():
    while True:
        try:
            # text = input('calc > ')
            text = """
BEGIN

    BEGIN
        number := 2;
        a := number;
        b := 10 * a + 10 * number / 4;
        c := a - - b
    END;

    x := 11;
END. """
        except EOFError:
            break
        if not text or text in 'q quit exit'.split():
            break
        calc_lexer = Lexer(text)
        parser = Parser(calc_lexer)
        calc_interpreter = Interpreter(parser)
        calc_interpreter.interpret()
        result = calc_interpreter.GLOBAL_SCOPE
        # result = calc_interpreter
        print(result)
        break


if __name__ == '__main__':
    main()
