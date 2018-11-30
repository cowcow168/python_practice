#private修飾子のようにできるかを実験で実装

class Test:
    __value = 'value'

    def __init__(self):
        print('init')

    def normal(self):
        print('normal')

    def __private(self):
        print('private')


t = Test()
#normalを呼び出す
t.normal()

#privateなので呼べない。
# t.__private()
#こっちもプライベートなので呼べない。
# t.__value

#ただ、絶対的なものでなく
t._Test__private()
t._Test__value

