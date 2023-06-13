operations = ['+', '-', '*', '/', '^', 'sin', 'cos', 'log', 'ln', 'tg', 'ctg',
              'arcsin', 'arccos', 'arctg', 'arcctg', '(', ')']
bin_func = ['+', '-', '*', '/', '^', 'log']
prefix_func = ['sin', 'cos', 'ln', 'tg', 'ctg', 'arcsin', 'arccos', 'arctg', 'arcctg']

priorities = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}

variable = 'x'


def diff_variable():
    return '1'


def diff_sum(operand1, operand2):
    return [*diff(operand1), *diff(operand2), '+']


def diff_minus(operand1, operand2):
    return [*diff(operand1), *diff(operand2), '-']


def diff_mul(operand1, operand2):
    return [*diff(operand1), *operand2, '*', *operand1, *diff(operand2), '*', '+']


def diff_division(operand1, operand2):
    return [*diff(operand1), *operand2, '*', *operand1, *diff(operand2), '*', '-', *operand2, '2', '^', '/']


def diff_pow(operand1, operand2):
    return [*operand1, *operand2, '^', 'e', *operand1, 'log', '*', *diff(operand2), '*', *operand2,
            *operand1, *operand2, '1', '-', '^', '*', *diff(operand1), '*', '+']


def diff_const():
    return '0'


def diff_sin(operand1):
    return [*diff(operand1), *operand1, 'cos', '*']


def diff_cos(operand1):
    return ['0', '1', '-', *diff(operand1), '*', *operand1, 'sin', '*']


def diff_log(operand1, operand2):
    return [*diff(operand2), *operand2, 'e', *operand1, 'log', '*', '/']


def diff_ln(operand1):
    return [*diff(operand1), *operand1, '/']


def diff_tg(operand1):
    return [*diff(operand1), *operand1, 'cos', '2', '^', '/']


def diff_ctg(operand1):
    return ['0', *diff(operand1), '-', *operand1, 'sin', '2', '^', '/']


def diff_arcsin(operand1):
    return [*diff(operand1), '1', *operand1, '2', '^', '-', '1', '2', '/', '^', '/']


def diff_arccos(operand1):
    return ['0', '1', '-', *diff(operand1), '*', '1', *operand1, '2', '^', '-', '1', '2', '/', '^', '/']


def diff_arctg(operand1):
    return [*diff(operand1), '1', *operand1, '2', '^', '+', '/']


def diff_arcctg(operand1):
    return ['0', '1', '-', *diff(operand1), '*', '1', *operand1, '2', '^', '+', '/']


def diff(argsInp):
    args = get_args_for_operations(argsInp)
    if args[-1] not in operations and args[-1] != variable:
        return diff_const()
    else:
        if args[-1] == variable:
            return diff_variable()
        elif args[-1] == '+':
            return diff_sum(args[0], args[1])
        elif args[-1] == '-':
            return diff_minus(args[0], args[1])
        elif args[-1] == '*':
            return diff_mul(args[0], args[1])
        elif args[-1] == '/':
            return diff_division(args[0], args[1])
        elif args[-1] == '^':
            return diff_pow(args[0], args[1])
        elif args[-1] == 'sin':
            return diff_sin(args[1])
        elif args[-1] == 'cos':
            return diff_cos(args[1])
        elif args[-1] == 'log':
            return diff_log(args[0], args[1])
        elif args[-1] == 'ln':
            return diff_ln(args[1])
        elif args[-1] == 'tg':
            return diff_tg(args[1])
        elif args[-1] == 'ctg':
            return diff_ctg(args[1])
        elif args[-1] == 'arcsin':
            return diff_arcsin(args[1])
        elif args[-1] == 'arccos':
            return diff_arccos(args[1])
        elif args[-1] == 'arctg':
            return diff_arctg(args[1])
        elif args[-1] == 'arcctg':
            return diff_arcctg(args[1])


# функция находит границы опреандов
def get_args_for_operations(args):
    if not args:
        return []
    index_of_second_operand = 0
    n = 0
    previous_operations_flag = False

    for i in range(2, len(args) + 1):
        if args[-i] in operations:
            if previous_operations_flag:
                n -= 1
            n += 2 if args[-i] in bin_func else 1
            previous_operations_flag = True
        else:
            if n == 0:
                index_of_second_operand = -i
                break
            n -= 1
        if n == 0:
            index_of_second_operand = -i
            break

    return args[:index_of_second_operand], args[index_of_second_operand:-1], args[-1]


# проверка на то, что ввод является числом
def isNumber(str):
    try:
        numb = float(str)
        return True
    except ValueError:
        return False


# упрощение выражение
def simplify_expr(argsInp, const=True):
    args = get_args_for_operations(argsInp)
    if not args:
        return []

    if len(args[0]) == 1 and len(args[1]) == 1 and isNumber(args[0][0]) and isNumber(args[1][0]):
        if args[-1] == '^':
            return [(str(eval(f'{args[0][0]}**{args[1][0]}')))]
        return [(str(eval(f'{args[0][0]}{args[-1]}{args[1][0]}')))]

    if args[-1] not in operations:
        return [args[-1]]

    elif args[-1] == '+':
        if args[0] == ['0']:
            return [*simplify_expr(args[1])]
        elif args[1] == ['0']:
            return [*simplify_expr(args[0])]

    elif args[-1] == '*':
        if args[0] == ['0'] or args[1] == ['0']:
            return ['0']
        elif args[0] == ['1']:
            return [*simplify_expr(args[1])]
        elif args[1] == ['1']:
            return [*simplify_expr(args[0])]

    elif args[-1] == '/':
        if args[0] == ['0']:
            return ['0']

    elif args[-1] == '-':
        if args[1] == ['0']:
            return [*simplify_expr(args[0])]

    elif args[-1] == 'ln':
        if args[1] == ['e']:
            return ['1']
        else:
            return [*simplify_expr(args[1]), args[-1]]

    elif args[-1] == 'log':
        if args[0] == ['e'] and args[1] == ['e']:
            return ['1']

    elif args[-1] == '^':
        if args[1] == ['1']:
            return [*args[0]]

    if const:
        return simplify_expr([*simplify_expr(args[0]), *simplify_expr(args[1]), args[-1]], False)

    return [*simplify_expr(args[0]), *simplify_expr(args[1]), args[-1]]


if __name__ == '__main__':
    pass
