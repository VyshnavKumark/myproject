from django.urls import path
from . import views

urlpatterns = [
 path("",views.createbook),
 path("authors/",views.createauthor,name='author'),
 path("listbook/",views.listbook),
 path("specbook/<int:books_id>/",views.specificbook,name='details'),
 path("updatbook/<int:book_id>/",views.updatebook,name='update'),
 path('deletebook/<int:book_id>/',views.deletebook,name='delete'),
]
