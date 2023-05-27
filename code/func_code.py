def f():
    s = '-- Inside f()'
    print(s)

print('Before calling f()')

f()

print('After calling f()')


def g():
    pass

g()


def my_f(qty, item='사과', price=5.67):
    print(f'{qty} {item} cost ${price:.2f}')


my_f(6, 'banana', 1.74)
my_f(5)
my_f(4, item='귤', price=4.88)

def d_list(x):
    r = []

    for i in x:
        r.append(i * 2)
    
    return r

a = [1, 2, 3, 4, 5]
b = d_list(a)
b

def my_avg(a, b, c):
    return (a + b + c) / 3

my_avg(1, 2, 3)

def avg(a):
    total = 0
    for v in a:
        total += v
    return total / len(a)

avg([1, 2, 3, 4, 5, 10])