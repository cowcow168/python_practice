#外部ライブラリーの管理

# conda update conda
# conda update anaconda


#freezeを使って書き出しておいたパッケージリストを全部インストール。
# pip freeze > package.txt
#
# 出力したパッケージリストをテキストファイルで保存しておくと、
# install -rを使ってパッケージを全部インストールできる。
#パッケージファイルに記載されたパッケージをインストールする。
# pip install -r package.txt
# pip install -r package.txt -r package_requirements.txt  ←複数指定可能
# ※pip自身や、setuptoolsなどのパッケージ管理ツールは表示されない。


# パッケージを検索する(PyPIで公開されているパッケージを検索する)
# pip search seaborn

# Gitのリポジトリをインストールする(GitHub上にあるリポジトリをインストールする例)
# pip install git+https://github.com/username/repository_name.git