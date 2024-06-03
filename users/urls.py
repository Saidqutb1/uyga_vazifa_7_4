from django.urls import path
from .views import UserView,UserDetailView,DeleteUserView,UpdateUserView,CreateUserView

urlpatterns = [
    path('users/',UserView.as_view()),
    path('users/<int:pk>/',UserDetailView.as_view()),
    path('users/<int:pk>/delete/',DeleteUserView.as_view()),
    path('users/<int:pk>/update/',UpdateUserView.as_view()),
    path('users/create/',CreateUserView.as_view()),
]