from django.urls import path
from .views import BooksDetailView, Bookslistview
urlpatterns = [

    path('',Bookslistview.as_view(), name="list"),
    path("<int:pk>", BooksDetailView.as_view(), name="detail" )

]