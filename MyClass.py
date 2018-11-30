#object.pyを改良する

class MyClass:
    string = ""

    #コンストラクタ(インスタンス作成時に呼び出されるメソッド)
    def __init__(self,string):
        print("__init__is called")
        self.string = string

    def set_string(self,string):
        self.string = string

    def get_string(self):
        return self.string

    def double(self):
        self.string *= 2

mc = MyClass("python")
get_str = mc.get_string()
print(get_str)
