============
乗ログアプリ
============

目的
=====


Webブラウザーでコメント投稿するWebアプリケーションの練習

ツールのバージョン
===================

:Python:        3.6.4
:pip:           9.0.1


インストールと起動方法
======================

リポジトリーからコードを取得し、その下にvenv環境を用意します::

 $ git clone https://github.com/tensho9408/norilog.git
 $ cd norilog 
 $ python3.6 -m venv venv
 $ source venv/bin/activate
 (venv) $ pip install .
 (venv) $ norilog
 * Runing on httpp://127.0.0.1:8000/

開発手順
==========

開発用インストール
==================

1. チェックアウトする
2. 以下の手順でインストール::

    (venv) $ pip install -e . 

依存ライブラリ変更時    
--------------------

1.  ``setup.py`` の ``install_requires`` を更新する
2. 以下の手順で環境を更新する::


       (venv) $ deactivate
       $ python3.6 - m venv --clear venv
       $ source venv/bin/activate
       (venv) $ pip install -e ./norilog
       (venv) $ pip freeze > requirements.txt

3. setup.pyとrequirements.txtをリポジトリーコミットする

