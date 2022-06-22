num = 1
name: str = '1'

new_num = int(num)

print(new_num, type(new_num))

# バックスラッシュNで改行を意味する
print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',', end='.\n')

# 数値
# 商のみを表示させたい場合//を二つ表示させる　割った後のあまりは％ 冪乗は＊＊
print(2 + 2)

import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# help(***)　を使用するとドキュメントが確認できる

print('hello')
print("hello")
print("i don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")
print('hello.\nHow are you?')
# rはrowデータの略　これで＼nの改行と認識されなくなる
print(r'C:\nam\name')

print("#############")
print("""\
line1
line2
line3\
""")
print("#############")

print('Hi.' * 3 + 'Mike')

s = ('aaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbb')

print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])

word = 'j' + word[1:]
print(word)
print(word[:])
n = len(word)
print(n)

s = 'My name is Mike.Hi Mike'
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

print('##################')
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
# 先頭のみ大文字にして他を小文字にて出力
print(s.capitalize())
# 全てのセンテンス頭を大文字に変える
print(s.title())
# 全て大文字
print(s.upper())
# 全て小文字
print(s.lower())
# 置き換え
print(s.replace('Mike', 'Nancy'))

'a is {2} {1} {0}'.format(1, 2, 3)

a = 'a'
print(f'a is {a}')
x, y, z = 1, 2, 3
print(f'a is {x}, {y},{z}')

name = 'jun'
family = 'Sakai'
print(f'My name is {name} {family}. watashi no namae ha {family} {name}.')

print(f'My name is {name} {family}. watashi no namae ha {family} {name}.')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))
print(r.count(3))

if 5 in r:
    print('exit')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My Name is Mike.'
# ’’の中を探して分ける
to_split = s.split(' ')
print(to_split)

# ''の中に入っている文字列の中で繋げる
x = '########'.join(to_split)
print(x)

i = [1, 2, 3, 4, 5]
j = i
# 配列jの中の一個目を１００に置き換える
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)

# 値渡しと参照渡し
# 値渡し
X = 20
Y = X
Y = 5
# どこに渡しているか参照
print(id(X))
print(id(Y))
print(X)
print(Y)

# 参照渡し
X = ['a', 'b']
Y = X
Y[0] = 'p'
# どこに渡しているか参照
print(id(X))
print(id(Y))
print(X)
print(Y)

num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)
x, y = (10, 20)
# print(x, y)と同様

min, max = 0, 100
print(min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp

print(i, j)
# 上のやり方だと文字を入れ替えるのにだいぶ手間がかかる

# 以下案パッキング参照
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

choose_from_two = ('a', 'b', 'c')

answer = []
answer.append('a')
answer.append('c')

print(choose_from_two)
print(answer)

# 参照渡し　後から入れても同一になってしまう
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

# 中身の検索がしやすい
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fruits['apple'])

# 集合の使用例
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)
# 重複したものからユニークを拾う型変換
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)

# １行が長くなるときはバックスラッシュをつかう
s = 'aaaaaaaaaaaaaaaaa' \
    + 'bbbbbbbbbbbbbb'
print(s)
# バックスラッシュ以外であればかっこでくくる
x = (1 + 1 + 1 + 1 + 1 + 1 + 1
     + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)

x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print(10)
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# if not a == b:
#      print('')
# 以下記述推奨　同じ意味
if a != b:
    print('')

a = 10
b = a ** 2
print(b)

a = 10
b = a ** 2
c = b % 20 + 5
d = 8
e = d / b
f = d // c
print('{0}, {1}'.format(e, f))

# is_okに空の変数が入っていなければtrueとなる
# False, 0, 0.0, '', [], (), {}, set()集合
is_ok = 0

if is_ok:
    print('OK!')
else:
    print('No!')

# 変数に何も入れたくない時
is_empty = None
# print(help(is_empty))

if is_empty is None:
    print('None!!')

# print(1 == True)
# isはオブジェクト同士が同じもの同士である
# print(1 is True)
print(True is True)

# count = 0
#
# while count < 5:
#     print(count)
#     count += 1

# count = 0
# while True:
#     # noinspection PyUnreachableCode
#     if count >= 5:
#         # while文を途中で抜けるさいはbreak
#         break
#
#         if count == 2:
#             count += 1
#             # ここで上に戻る
#             continue
#
#         print(count)
#         count += 1

count = 0

while count < 5:
    print(count)
    count += 1
# elseはwhile文を抜けなければ実行される
else:
    print('done')

# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
# 上と同義の記述　for in 次々と入力していくことをイテレーターという
for i in some_list:
    print(i)
# for ループ文の中にもbreak は入力可能

word = ['MY', 'Name', 'is', 'Mike']

for s in word:
    if word == 'Name':
        # 繰り返しを抜ける　break
        # 下に行かず次にいくのがcontinue
        continue

    print(s)

# for else文
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)

else:
    print('I ate all!!!')

# range関数
# 0から順に入力してくれる。始めの数字を０以外にするには（2, 10)のように記入する
# 3個飛ばしとかで入力する場合は、(2, 10, 3)と記述する
for i in range(10):
    print(i)

for i in range(10):
    print(i, 'hello')

# enumerate関数
# 複数の関数を自動入力してくれる
# i = 0
# for fruit in ['apple', 'banana', 'orange']:
#     print(i, fruit)
#     i += 1

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# zip関数
days = ['mon', 'tue', 'wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']
# for i in range(len(days))
#     print(days[i], fruits[i], drinks[i])

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dictionaly を　for ループするには
d = {'x': 100, 'y': 200}
for k, v in d.items():
    print(k, ':', v)


def say_something():
    print('hi')
    #
    # f = say_something()
    # f()

    s = 'hi'
    return s


result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "T don't know"


result = what_is_this('red')
print(result)


# num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b


r = add_num(10, 20)
print(r)


# 位置引数とキーワード引数とデフォルト引数
def menu(entree, drink, dessert):
    print(entree)
    print(drink)
    print(dessert)


menu('beef', 'beer', 'ice')


# デフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)


menu(entree='chiken')


# デフォルト引数で気をつけること
# リストはデフォルト引数で与えない
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


# y = [1, 2, 3]
r = test_func(100)
print(r)


# 位置引数のタプル化
def say_something(word, *args):
    print('word =', word)
    # argsに入るのは全てタプル型となる
    for arg in args:
        print(arg)


say_something('Hi!', 'Mike', 'Nance')


# キーワード引数の辞書化
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


# menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)


def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu('banana', 'apple', 'orange', entree='beef', drink='coffee')


# docstringsとは
def example_func(param1, param2):
    """Example function with types documented in the docstring.
    Args:
        param1(int): The first parameter.
        param2(str): Yhe second parameter.

    Returns:
         bool: The return value. True for success, False otherwise.

    """
    print(param1)
    print(param2)
    return True


example_func.__doc__


# 関数内関数
def outer(a, b):
    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)


outer(1, 2)


# クロージャー
# def outer(t, u):
#     def inner():
#         return t + u
#
#     return inner
#
#
# f = outer(1, 2)
#
# print('######')
#
# r = f()
# print(f)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

# デコレーター
def print_more(func):
    def wrpper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrpper

def print_info(func):
    def wrpper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrpper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# ラムダ
l = ['Mon', 'Tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def chande_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     # capitalize 大文字にする
#     return word.capitalize()

chande_words(l, lambda word: word.capitalize())
chande_words(l, lambda word: word.lower())

# ジェネレーター
# forループの場合、一気に回るがジェネレーターは何かをはさんでも繰り返し実行できる
l = ['Good morining', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('##############')

# ジェネレーターでの実行

def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    # yield がジェネレーターの判断となる
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print('@@@@')

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


print('@@@@')

print(next(g))

# リスト内包表記
t = (1, 2, 3, 4, 5)
# タプル

r = []
for i in t:
    if i % 2 == 0:
        # 末尾に要素を追加 append
        r.append(i)
print(r)

r = [i for i in t if i % 2 == 0]
print(r)

# 例２
r = []
for i in t:
    for j in t2:
        r.append(i * j)

print(r)

r = [i * j for i in t for j in t2]

print(r)
