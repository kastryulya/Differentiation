# Differentiation

Development of the differentiation calculator for the course "Python".

Авторы: Коршунова Ульяна, Воронина Татьяна.

### Требования

1. Проверка корректности ввода с указанием позиции ошибки
2. Вычисление производной
3. Вывод результат в математической форме
4. Вычисление частных производных
5. Произведение сложный функций
6. Поиск кратных производных (f', f'', f'''...)

### Примеры запуска

1. Найти производную функции одной переменной f(x):

```
python3 diff.py '2x^3-4x^2+12x'
```

2. Найти частную производную функции двух переменных f(x, y) по заданной переменной:

```
python3 diff.py '2x^3-4x^2+12x' -var 'y'
```

3. Найти производную функции заданного порядка:

```
python3 diff.py '2x^3-4x^2+12x' -ord 3
```

4. Найти частную производную функции двух переменных f(x, y) по заданной переменной заданного порядка:

```
python3 diff.py '2x^3-4x^2+12x' -var 'y' -ord 3
```

### Правила ввода выражения

* Логарифм записывать в виде `log(2)(3x)`, где `(2)` - основание (_**обязательно в скобках**_), `(3x)` - аргумент.
* Знаки умножения можно опускать **только** между числовыми коэффициентами и функцией/переменной/скобками.
  **Неправильно:** `(56xy/(12x-1))(2x\*sin(y)+4)`. **Правильно:** `(56x*y/(12x-1))\*(2x\*sin(y)+4)`.
* Отрицательные числа вводить в форме `(0-3)`


### Подробности реализации

Вычисления производной, преобразования и упрощения выражений происходит при помощи
обратной польской нотации.

* `Diff.py`- Точка входа в программу.
* `Rpn.py` - Реализация всех преобразований, связанных с обратной польской нотацией (Reverse Polish notation, RPN).
* `Differentiation.py` - Реализация процесса дифференцирования.
* `Incorrect_input.py` - Обработка входного выражения, нахождение ошибок ввода.
* `Test/Differentiation_test.py` - Тестирование процесса дифференцирования.
* `Test/Incorrect_input_test.py` - Тестирование обработки входных выражений

Покрытие тестами составляет 98%.
