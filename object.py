#関数チックな考え方仕事をさせる(部下A、仕事)
# オブジェクト指向の考え方(「部下A」に「仕事をさせる」(仕事))

# 関数は、オブジェクトを引数
# メソッドは、オブジェクトから処理を呼び出す。
string = "hello world python"
#関数(処理にデータを与える。データと処理の結びつきが弱い)
length = len(string)
#メソッド(splitは、stringにしか使えない。データとの結びつきが強い)
words = string.split()
print(words)

class MyClass:
    string = ""

    def set_string(self,string):
        self.string = string

    #属性へのアクセスself.属性(しないと関数だけのローカル変数となる。)
    def get_string(self):
        return self.string

    def double(self):
        self.string *= 2

#インスタンス化
mc = MyClass()

mc.set_string("hello")
mc.double()
print(mc.get_string())



class Counter:
    counter = 1
    #現在のカウント値を返す
    def get_value(self):
        return self.counter
    #現在のカウント値を+1する。
    def count_up(self):
        self.counter = self.counter + 1
        return self.counter
    #カウンタを1に戻す
    def clear_counter(self):
        self.counter = 1
        return self.counter

ct = Counter()
get_number = ct.get_value()
ct.count_up()
count_number = ct.count_up()
print(get_number)
print(count_number)
clear_count = ct.clear_counter()
print(clear_count)






