a = lambda x: x + 1

a(1)
a(41)
a(3)
a(19)

(lambda x, y: x + y + 10)(3, 7)


f_name = lambda first, last: f'full name: {first.title()}, {last.title()}'
f_name('guido', 'van rossum')

(lambda x, y, z: x + y - z)(10, 4, 7)
(lambda x, y, z=3: x + y - z)(10, 4)
(lambda x, y, z=3: x + y - z)(1, y=10)

(lambda *args: sum(args))(1, 2)
(lambda *args: sum(args))(1, 2, 3)
(lambda *args: sum(args))(1, 2, 10, 20)
(lambda *args: sum(args))(1, 2, 4, 8, 9)

(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

numbers = [1, 2, 3, 4, 5]
squared = []

for num in numbers:
    squared.append(num ** 2)

squared

def square(number):
    return number ** 3

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

list(squared)

squared

numbers = [1, 2, 3, 4, 5]

squared = map(lambda x: x ** 3, numbers)
list(squared)

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

list(map(lambda x, y: y - x, a, b))

numbers = [-2, -1, 0, 1, 2]
abs_value = list(map(abs, numbers))
abs_value

list(map(float, numbers))

words = ['welcome', 'to', 'real']
list(map(len, words))