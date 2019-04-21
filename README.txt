このリポジトリは、Qiitaに投稿されたDjangoのチュートリアルを実装したものです。
ただし「(6)スマホAPI」については実装できていません。

■参照したチュートリアル - Python Django入門 (Qiita)
(1)はじめに
   https://qiita.com/kaki_k/items/511611cadac1d0c69c54
(2)Python環境のインストール
   https://qiita.com/kaki_k/items/1fff7fefcf26dc4b69bc
(3)Djangoを始める
   https://qiita.com/kaki_k/items/7b178ad39394a031b50d
(4)Bootstrap、DjangoのCRUD
   https://qiita.com/kaki_k/items/6e17597804437ef170ae
(5)CRUD続き
   https://qiita.com/kaki_k/items/ebc8d8b07434e1721756
(6)スマホAPI
   https://qiita.com/kaki_k/items/b76acaeab8a9d935c35c

■実行環境
・Python 3.6.8
・Django 1.11.20
・django-bootstrap4 0.0.8
Mezzanineと一緒に動作させるため、Django 1.x系を前提にしています。
Windows10でcondaで環境設定を行い、ローカル環境で動作確認できています。

■実行方法
(1)Cloneする
(2)本番環境の場合は
・mysite/settings.pyのALLOWED_HOSTSを設定
(3)Djangoの設定
python manage.py makemigrations cms
python manage.py migrate
python manage.py createsuperuser
(4)実行
python manage.py runserver
ブラウザからアクセス
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/cms/book/

