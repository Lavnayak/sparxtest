from django import forms
from .models import MyUser, TransactionUser

# class TransactionUserForm(forms.ModelForm):
#     class Meta:
#         model = TransactionUser
        

#     def __init__(self, user, *args, **kwargs):
#         super(TransactionUserForm, self).__init__(*args, **kwargs)
#         self.fields[''].queryset = MyUser.objects.filter(=user)