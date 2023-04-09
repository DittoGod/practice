def a():
    print('a() was called.')
    b()
    print ('a() is returning.')

def b():
    print('b() wsa called.')
    c()
    print('b() is returning.')

def c():
    print('c() was called.')
    print('c() is returning.')

a()