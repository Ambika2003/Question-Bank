from  django import forms
from .models import User
from .models import Question, Option

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
        #exclude=('name',) to exclude any field 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'subject']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']




