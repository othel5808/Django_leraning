from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST" or request.method == 'post':
        # return render(request, 'accountapp/hello_world.html', context={'text': 'POST method!!'})
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list })
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list })


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # form_calss = UserCreationForm
    # reverse는 클래스 베이스 뷰에서 사용이 불가능, 따라서 _lazy는 클래스 대응이라고 생각하면 됨.
    success_url = reverse_lazy('accountapp:hello_world')
    # 어느 HTML을 통해서 봐야할지
    # template_name='accountapp/create.html'
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    # 템플릿에서 사용하는 유저 객체의 이름을 설정 할 수 있음
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

