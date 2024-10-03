from django import forms

from budget.models import Expense

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