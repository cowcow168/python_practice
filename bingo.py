#ビンゴマシンを作成する。
# 一度出たものは、出力させないようにして、ボールがなくなったらボールがありませんと表示させる。ボールに書いてある数字を出す
# マシーンに入っているボールの数は変動できるようにする
import random

class BingoMachine:
    ballList = []

    def __init__(self,min,max):
        self.ballList = list(range(min,max+1))

    def getBall(self):
            if(len(self.ballList) == 0):
                message = "ボールが入っていません。"
                return message
            index = int(random.uniform(0,len(self.ballList)))
            #リストから要素を取り出して、それと同時に要素を削除する
            return self.ballList.pop(index)

#対話型以外でなく、ファイルから実行する時には必要
b = BingoMachine(1,5)
Length =len(b.ballList)
# print(Length)
for i in range(Length +1):
  b.getBall()