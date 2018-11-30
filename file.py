#ファイル処理の流れ
# 1：fileをオープンしてfileオブジェクトを取得
# 2：fileオブジェクトに対して処理を行う
# 3：fileをクローズする

#ファイルオブジェクトの作成
# open(ファイルパス,オープンするモード)
# r:読み込みモード
# w:新規書き込みモード
# a:追加書き込みモード

#ファイルオブジェクトのクローズ
# f.close()

#読み込み処理
f = open("file.txt","r")
#一行読み込み
print(f.readline())
print(f.readline())
#全ての行をlistとして読み込み
print(f.readlines())

#ファイルの書き込み処理(closeしないで問題になるのは、Pythonプロセス起動しっぱなしで1万個のファイルを開きっぱなし
# にした場合同時に開けるファイルの数の上限に達する場合
# ファイルを開いた変数を保持していなければ順次開放されていくため、これもすぐには問題になりません。
# ただ、順次開放を待つのではなく使い終わったら明示的にcloseする方が良い、という観点で説明するのは良い修正
f2 = open("file2.txt","w")
f2.write("hello")
f2.write("world")
f2.write("/n")
wist = ["abc","def","ghi"]
f2.writelines(wist)
f2.flush()
f2.close()