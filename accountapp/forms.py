from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 상위 내용중 username field를 비활성화 하도록 설정
        self.fields['username'].disabled = True
        