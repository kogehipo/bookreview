from django.conf.urls import url
# from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    # Django v1系ではpath()ではなくurl()を使う
    # 下の例ではbook/の後に$が必要。そうしないとbook/add/の場合でもbook/にマッチしてしまう。
    # 正規表現の中での引数(番号)の渡し方が違う

    # bool_list()はページネーションせずに全部一覧表示する
    # url(r'^book/$', views.book_list, name='book_list'),   # 一覧
    url(r'^book/$', views.BookList.as_view(), name='book_list'),  # 一覧

    url(r'^book/add/$', views.book_edit, name='book_add'),  # 登録
    url(r'^book/mod/(?P<book_id>[0-9]+)/$', views.book_edit, name='book_mod'),  # 修正
    url(r'^book/del/(?P<book_id>[0-9]+)/$', views.book_del, name='book_del'),   # 削除

    # 感想
    url(r'^impression/(?P<book_id>[0-9]+)/$', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    url(r'^impression/add/(?P<book_id>[0-9]+)/$', views.impression_edit, name='impression_add'),        # 登録
    url(r'^impression/mod/(?P<book_id>[0-9]+)/(?P<impression_id>[0-9]+)/$', views.impression_edit, name='impression_mod'),  # 修正
    url(r'^impression/del/(?P<book_id>[0-9]+)/(?P<impression_id>[0-9]+)/$', views.impression_del, name='impression_del'),   # 削除
]

#urlpatterns = [
#    # 書籍
#    path('book/', views.book_list, name='book_list'),   # 一覧
#    path('book/add/', views.book_edit, name='book_add'),  # 登録
#    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
#    path('book/del/<int:book_id>/', views.book_del, name='book_del'),   # 削除
#
#    # 感想
#    path('impression/<int:book_id>/', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
#    path('impression/add/<int:book_id>/', views.impression_edit, name='impression_add'),        # 登録
#    path('impression/mod/<int:book_id>/<int:impression_id>/', views.impression_edit, name='impression_mod'),  # 修正
#    path('impression/del/<int:book_id>/<int:impression_id>/', views.impression_del, name='impression_del'),   # 削除
#]
