import sys
from Differentiation import isNumber

smbls = ['+', '-', '*', '/', '^', 'sin', 'cos', 'log', 'ln', 'tg', 'ctg',
         'arcsin', 'arccos', 'arctg', 'arcctg', '(', ')', 'x', 'y', 'e']
bin_func = ['+', '-', '*', '/', '^']
prefix_func = ['sin', 'cos', 'ln', 'tg', 'ctg', 'arcsin', 'arccos', 'arctg', 'arcctg', 'log']


def input_is_correct(input):
    signs = signs_are_correct(input)
    brackets = brackets_are_correct(input)
    smbls = smbls_are_correct(input)

    idx_signs = sys.maxsize
    idx_brackets = sys.maxsize
    idx_smbls = sys.maxsize

    if not signs[0]:
        idx_signs = signs[1]
    if not brackets[0]:
        idx_brackets = brackets[1]
    if not smbls[0]:
        idx_smbls = smbls[1]

    if idx_signs == idx_brackets == idx_smbls == sys.maxsize:
        return [True, 0]

    return [False, min(idx_smbls, idx_signs, idx_brackets)]


# проверка корректности знаков
def signs_are_correct(input):
    prev_bin_func = True
    prev_prefix_func = True
    prev_opening_bracket = True

    for i in range(len(input)):
        if input[i] in bin_func:
            if prev_opening_bracket or prev_bin_func or prev_prefix_func:
                return [False, i]
            prev_bin_func = True
        elif input[i] in prefix_func:
            prev_prefix_func = True
        elif input[i] == ')':
            if prev_bin_func or prev_prefix_func or prev_opening_bracket:
                return [False, i]
        elif input[i] == '(':
            prev_opening_bracket = True
        else:
            prev_bin_func = False
            prev_prefix_func = False
            prev_opening_bracket = False

    if prev_bin_func or prev_prefix_func:
        return [False, len(input) - 1]
    return [True, 0]


# проверка корректности скобок
def brackets_are_correct(input):
    stack = []
    for i in range(len(input)):
        try:
            if input[i] == '(':
                stack.append([input[i], i])
            elif input[i] == ')':
                stack.pop()
            else:
                continue
        except IndexError:
            return [False, i]

    if not stack:
        return [True, 0]
    return [False, stack[-1][1]]


# проверка корректности символов
def smbls_are_correct(input):
    for i in range(len(input)):
        if input[i] not in smbls and not isNumber(input[i]):
            return [False, i]
    return [True, 0]


if __name__ == '__main__':
    pass
