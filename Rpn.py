import re
from Differentiation import isNumber

operations = ['+', '-', '*', '/', '^', 'sin', 'cos', 'log', 'ln', 'tg', 'ctg',
              'arcsin', 'arccos', 'arctg', 'arcctg', '(', ')']
bin_func = ['+', '-', '*', '/', '^', 'log']
prefix_func = ['sin', 'cos', 'tg', 'ctg', 'arcsin', 'arccos', 'arctg', 'arcctg', 'ln']
priorities = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0, 'log': 3}
variables = 'xy'


# сравнение приоритетов операций
def compare_priorities(op1, op2):
    return priorities[op1] >= priorities[op2]


# функция преобразования списка операций и операндов в обратную польскую нотацию
def opn(input):
    lst = reformat_expr(input)
    stack = []
    result = []

    while lst:
        smbl = lst.pop(0)
        if smbl not in operations or smbl in variables:
            result.append(smbl)
        elif smbl in prefix_func:
            stack.append(smbl)
        elif smbl == '(':
            stack.append(smbl)
        elif smbl == ')':
            head_of_stack = ''
            try:
                while head_of_stack != '(':
                    head_of_stack = stack.pop()
                    if head_of_stack != '(':
                        result.append(head_of_stack)
            except IndexError:
                print('Wrong input')
        elif smbl in bin_func:
            try:
                while stack[-1] in prefix_func or compare_priorities(stack[-1], smbl):
                    result.append(stack.pop())
            except IndexError:
                pass
            stack.append(smbl)

    while stack:
        result.append(stack.pop())

    return result


# функция преобразования обратной польской нотации в формат математического выражения
def from_opn(input):
    stack = []
    for i in input:
        if isNumber(i) or i in variables or i == 'e':
            stack.append(i)
            continue
        elif i in bin_func:
            a = stack.pop()
            b = stack.pop()
            if i == 'log':
                stack.append('({}{}{})'.format(i, b, a))
            else:
                stack.append('({}{}{})'.format(b, i, a))
        elif i in prefix_func:
            a = stack.pop()
            stack.append('({}{})'.format(i, a))
    return stack[0]


# функция заключает числовые множители в скобки
def adding_parentheses(input):
    input_with_parentheses = ''

    for i in range(len(input)):
        try:
            char = input[i]
            if isNumber(char):
                if not isNumber(input_with_parentheses[-1]):
                    input_with_parentheses += '('
                input_with_parentheses += char
                if input[i + 1] in operations or input[i + 1] in variables:
                    input_with_parentheses += ')'
            else:
                input_with_parentheses += char
        except IndexError:
            if i == 0:
                input_with_parentheses += char
                continue
            break

    if isNumber(input_with_parentheses[-1]):
        input_with_parentheses += ')'
    return input_with_parentheses


# функция перерабатывает строку выражения в список операций и операндов
def get_list_of_operations_and_operands(input):
    list_of_operations_and_operands = []
    i = 0
    input = input.replace(' ', '')

    while True:
        try:
            if input[i] in variables or input[i] in operations:
                list_of_operations_and_operands.append(input[i])
                i += 1
            elif isNumber(input[i]):
                temp_numb = ''
                try:
                    while isNumber(input[i]):
                        temp_numb += input[i]
                        i += 1
                    list_of_operations_and_operands.append(temp_numb)
                except IndexError:
                    list_of_operations_and_operands.append(temp_numb)
            else:
                if input[i].isalpha():
                    temp_fun = ''
                    try:
                        while input[i].isalpha():
                            temp_fun += input[i]
                            i += 1
                        list_of_operations_and_operands.append(temp_fun)
                    except IndexError:
                        list_of_operations_and_operands.append(temp_fun)
                else:
                    list_of_operations_and_operands.append(input[i])
                    i += 1
        except IndexError:
            break

    return list_of_operations_and_operands


# функция добавляет знаки умножения между числовыми множителями и функциями\переменной
def add_mult_signs(input):
    regex1 = r'\d+[(a-zA-Z]'  # нахождение числовых множителей
    prev_input = input.replace(' ', '')
    count_of_mul = 0
    for m in re.finditer(regex1, prev_input):
        temp_input = prev_input[:m.end() - 1 + count_of_mul]
        temp_input += '*'
        temp_input += prev_input[m.end() - 1 + count_of_mul:]
        prev_input = temp_input
        count_of_mul += 1

    regex2 = r'\(.*?\)+\w'  # нахождение скобок как множителей
    count_of_mul = 0
    for m in re.finditer(regex2, prev_input):
        temp_input = prev_input[:m.end() - 1 + count_of_mul]
        temp_input += '*'
        temp_input += prev_input[m.end() - 1 + count_of_mul:]
        prev_input = temp_input
        count_of_mul += 1

    regex3 = rf'[xy]\(.*?\)+'  # нахождение скобок как множителей
    count_of_mul = 0
    for m in re.finditer(regex3, prev_input):
        temp_input = prev_input[:m.start() + 1 + count_of_mul]
        temp_input += '*'
        temp_input += prev_input[m.start() + 1 + count_of_mul:]
        prev_input = temp_input
        count_of_mul += 1

    return prev_input


# функция форматирует исходное выражение в список операций и операндов
def reformat_expr(input):
    return get_list_of_operations_and_operands(adding_parentheses(add_mult_signs(input)))


if __name__ == '__main__':
    pass
