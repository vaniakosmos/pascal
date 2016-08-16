from calc.interpreter import Interpreter


def main():
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if not text or text == 'q':
            break
        calc_interpreter = Interpreter(text)
        result = calc_interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
