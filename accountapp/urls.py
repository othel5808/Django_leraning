from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # as_view() 를 적어야, 함수형 view 처럼 동작
    path('create/', AccountCreateView.as_view(), name='create')
]