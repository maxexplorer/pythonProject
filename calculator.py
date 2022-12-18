# Calculator


def calculator(expression: str):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Expression should contain at least one sign {allowed}')

    for sign in allowed:
        if sign in expression:
            try:
                left, right = map(int, expression.split(sign))
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Expression should contain two integer numbers and at least one arithmetic operator')


if __name__ == '__main__':
    print(calculator('5*5'))





