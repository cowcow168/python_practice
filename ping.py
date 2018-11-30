#pingのプログラム(scriptをパラメータつきで起動する。スクリプト内に直接書き込むより融通生がある。
#1:宛先を引数で受け取る
#2:宛先へrequestを送る。
#3:宛先からresponseを受け取る
#4:受信結果を表示

#コマンドライン引数にアクセスするためのモジュール
import sys
#正規表現をするために必要
import re

#事前に検索パターンをコンパイルしておく方法(同じパターンで何度も検索する場合に、毎回パターンを指定する必要なく、検索できるので早い。)
patern = r"exit"
repatern = re.compile(patern)
length=input("文字を入力してください。")
exit_flag = repatern.match(length)
if exit_flag:
    #処理を終了させる
    # sys.exit()
    sys.exit(1) #終了させた時に返却する値を設定。exitでなく、エラーが出たなどと出力させたい時に使う
print(len(length))