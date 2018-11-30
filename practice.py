#coding: UTF-8

#偶数か奇数を出す
for i in range(10):
    if(i%2 == 0):
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))
print("done")


#文字列の処理

word = "hello world"
#置き換え
replace=word.replace("world","python")
print(replace)

#分割(空白で分割)
split=word.split(" ")
print(split)

#含むか
search_word = "hell"

exists_flag = search_word in word
print(exists_flag)

#位置
position = word.find("o")
none = word.find("X")
print(position)
#文字列に含まれていない時は、-1
print(none)