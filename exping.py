#パス(os上のファイルやディレクトリの所在地を示す)
# 絶対パス:ルートからたどるパス
# 相対パス:現在の自分の位置からたどるパス
# ./自分がいるディレクトリ
# ../自分の上の階層のディレクトリ

# 現在のカレントディレクトリを取得:os.getcwd()
# ディレクトリの移動:os.chdir(移動先のパス)
# 絶対のパスの取得:os.path.abspath(path) os.path.abspath("practice")
# os非依存のパスの取得方法os.path.join(TUPLE)
# ファイル or ディレクトリの存在確認:os.path.exists(パス) os.path.exists("/Users/ushijima") 返り値boolean
# ディレクトリか:os.path.isdir(パス)
# ファイルか:os.path.isfile(パス) os.path.isfile("/Users/ushijima") 返り値boolean
# ディレクトリの作成:os.mkdir(ディレクトリのパス)
# ディレクトリの削除:os.rmdir(ディレクトリのパス)
# ディレクトリの中身一覧(リストに格納されて返される):os.listdir("./")
# ファイル、ディレクトリの削除:os.remove(パス)
# ディレクトリの再帰的削除:os.removedirs(パス)

#シェルスクリプト:シェル自体を操作するプログラミングスタイル
# シェルスクリプト記述のコツ
# ・可能な限り既存のコマンドを使う
# ・コマンドとコマンドの接続にpythonを使う
# (1)結果 = コマンドの発行
# (2)結果を処理
# (3)処理結果にもとづいて次のコマンドを作成
# (4)(1)へ


# コマンドの呼び出し
# os.system("コマンド"):出力が不要な場合
# commands.getoutput("コマンド"):出力が必要な場合

#複数の宛先のping到達率を測定

#バグがあり、修正する必要があり
import subprocess

def ping(dest):
    result = subprocess.check_output("ping -n 3 {}".format(dest))
    print(result)
    lines = result.split(" ")
    length = len(lines)
    packetLoss = lines[length-2].split()[6]
    rtt = lines[length - 1].split()[3].split("/")[1]
    return (dest,packetLoss,rtt)

dests = ["google.com","yahoo.com"]
for dest in dests:
    print(ping(dest))