from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # as_view() 를 적어야, 함수형 view 처럼 동작
    path('create/', AccountCreateView.as_view(), name='create'),
    # detail 페이지 구성 : 단, 특정 계정에 대한 detail을 보아야하기 때문에, primarykey를 받아야한다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name="detail"),
    path('update/<int:pk>', AccountUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name="delete")
]