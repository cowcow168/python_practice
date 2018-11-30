#素数を出す(約数に1とその数自体以外を持たないこと。
# n = int(input("範囲を指定してください。>"))
#2からスタートiは、割られる数
# for i in range(2, n):
#     #jは、割る数
#     for j in range(2, i+1):
#         if i % j == 0:
#             if i == j:
#                 print(i)
#             else:
#                 break

#最後にまとめて出力する方法
# n = int(input("範囲を指定してください。>"))
# primeN = []
# for i in range(2,n):
#     for j in range(2,i+1):
#         # 初めてjで割り切れた時
#         if i % j == 0:
#             if i == j:
#                 primeN.append(i)
#             else:
#                 break
# for i in primeN:
#     print(i)

#上記では、数が多くなれば遅くなる。


#素数のリストを使って効率よく素数を求めてみる。
# 素数をリストにすると、今まで求めた素数で割れるか割れないかを調べるだけで、次の素数を求めることができる。

#素数のリスト [2, 3, 5] がある
#  6 を素数のリストに含まれる数字で割ろうとすると、2 もしくは 3 で割り切れるので、6 は素数ではありません。
# 次に、1 増やして
# 7 を素数のリストに含まれる数字で割ってみます。どの数字でも割ることができないので、7 は素数であることが分かります

#最初に2だけを素数リストの要素に用意しておくと、後は自動的に素数をリストに追加してくれる

n = int(input("範囲を指定してください。>"))
primeN =[2]
for i in range(2,n):
    for j in range(len(primeN)):
        if i % primeN[j] == 0:
            break
        else:
            if j == len(primeN) -1:
                primeN.append(i)
for i in primeN:
    print(i)

