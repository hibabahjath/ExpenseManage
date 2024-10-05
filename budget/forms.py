from django import forms

from budget.models import Expense

from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):

    class Meta:

        model=Expense

        # fields="__all__"

        exclude=("created_date",)

        widgets={

            "title":forms.TextInput(attrs={"class":"form-control"}),

            "amount":forms.NumberInput(attrs={"class":"form-control"}),

            "category":forms.Select(attrs={"class":"form-control form-select"}),

            "user":forms.TextInput(attrs={"class":"form-control"}),
        }

class RegistrationForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["first_name","last_name","email","username","password"]

        widgets={

        "first_name":forms.TextInput(attrs={"class":"form-control"}),

        "last_name":forms.TextInput(attrs={"class":"form-control"}),

        "email":forms.EmailInput(attrs={"class":"form-control"}),

        "username":forms.TextInput(attrs={"class":"form-control"}),

        "password":forms.TextInput(attrs={"class":"form-control"}),

        }

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

    widgets={

        "username":forms.TextInput(attrs={"class":"form-control"}),

        "password":forms.TextInput(attrs={"class":"form-control"})
    }