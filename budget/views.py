from django.shortcuts import render,redirect

from django.views.generic import View

from budget.forms import ExpenseForm

from django.contrib import messages

from budget.models import Expense

# Create your views here.

class ExpenseAddView(View):

    def get(self,request,*args,**kwargs):

        form_instance=ExpenseForm()

        return render(request,"expense_create.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid:

            form_instance.save()

            messages.success(request,"Added succesfully")

            return redirect('exp-all')
        
        else:

            messages.error(request,"Added failed")

            return render(request,"expense_create.html",{"form":form_instance})
        
class ExpenseListView(View):
        
    def get(self,request,*args,**kwargs):

        search_txt=request.GET.get("search_text")

        selected_category=request.GET.get("category","all")

        if selected_category == "all":

            qs=Expense.objects.all()

        else:

            qs=Expense.objects.filter(category=selected_category)

        if search_txt != None:

            qs=Expense.objects.filter(title__icontains=search_txt)

        return render(request,"expense_list.html",{"expense":qs,"selected":selected_category})
    
class ExpenseDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Expense.objects.get(id=id)

        return render(request,"expense_detail.html",{"form":qs})
    
class ExpenseUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        exp_obj=Expense.objects.get(id=id)

        form_instance=ExpenseForm(instance=exp_obj)

        return render(request,"expense_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        form_instance=ExpenseForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Expense.objects.filter(id=id).update(**data)

            messages.success(request,"Added succesfully")


            return redirect('exp-all')
        
        else:

            messages.error(request,"error")

            return render(request,"expense_edit.html",{"form":form_instance})
        
class ExpenseDeleteView(View):

    def get(self,request,*args,**kwargs):

        Expense.objects.get(id=kwargs.get("pk")).delete()

        messages.success(request,"Deleted succesfully")


        return redirect('exp-all')
    

    
