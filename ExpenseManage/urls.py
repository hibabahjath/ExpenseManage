"""
URL configuration for ExpenseManage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budget import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.ExpenseAddView.as_view(),name="exp-add"),
    path('all/',views.ExpenseListView.as_view(),name="exp-all"),
    path('exp/<int:pk>/update/',views.ExpenseUpdateView.as_view(),name="exp-edit"),
    path('exp/<int:pk>/delete/',views.ExpenseDeleteView.as_view(),name="exp-delete"),
    path('register/',views.SignUpView.as_view(),name="register"),
    path('',views.SignInView.as_view(),name="login"),
    path('logout/',views.SignOutView.as_view(),name="logout"),
    path('summary/',views.ExpenseSummaryView.as_view(),name="summary"),


]
