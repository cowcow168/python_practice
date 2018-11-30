#coding: UTF-8


#python2系では、上記でよいが、3系では、文字列として渡されるので数値に変換する必要あり

# a,b = input("a:"),input("b:")
a,b =int(input("a:")),int(input("b:"))


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(a,b))