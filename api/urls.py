from django.conf.urls import url
#from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    # 書籍
    #path('v1/books/', views.book_list, name='book_list'),   # 一覧
    url(r'^v1/books/$', views.book_list, name='book_list'),   # 一覧
]
