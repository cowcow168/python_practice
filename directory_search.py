#現在のディレクトリ以下の構造を書き出すプログラム(pythonでファイルやディレクトリ(フォルダが存在するかどうか確認)

#OSによって異なるパス名の決まりがあるため、標準ライブラリのosを使用することで、Pythonが動作しているOSに適したパスになる
import os

#ちなみに公式ドキュメントでは、下記のように定義されているみたいです。
# posixpath UNIX スタイルのパス用
# ntpath Windows パス用
# macpath 古いスタイルの MacOS パス用

class ListFile:
    def __init__(self,path):
        self.path = path

    def printDir(self):
        #カレントディレクトリのパスを表示
        print("[{}]".format(self.path))
        #パスに存在するファイル名やディレクトリ名を取得
        for fileName in os.listdir(self.path):
            print(fileName)
        for fileName in os.listdir(self.path):
            #パスが存在しているディレクトリであるかを確認
            if os.path.isdir(fileName):
                #abspath(パス名)で正規化された絶対パスを返す
                lf = ListFile(os.path.abspath(fileName))
                #ディレクトリを再起的に読み込ませてファイル名を表示させる。
                lf.printDir()

#現在いるカレントディレクトリを取得する
lf = ListFile(os.getcwd())
#データなどをサーバーで取得した時に分析用データなど置き場所を決めてそこをカレントディレクトリにしたい時は,
# 下記のように移動する処理を追加する
# lf = ListFile(os.chdir("指定したいパス名"))
lf.printDir()

