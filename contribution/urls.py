"""lep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
# from .views import( EmployeeCreateView,
# EmployeeListView,
# EmployeeDetailView,
# EmployeeUpdateView

# )

app_name = 'contribution'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',EmployeeListView.as_view(),name='list-employee'),
    path('create/',views.FirmAutocomplete.as_view(),name='create-employee'),
    path('validate_firm/', views.validate_firm, name='validate_firm'),
    path('search/', views.autocompleteModel, name='autocomplete_employee'),
    path('firm_choice/', views.firm_choice, name='firm_choice'),
    path('formset/',views.formset_view,name='create-firm'),

    # path('<int:id>/',EmployeeDetailView.as_view(),name='employee-detail'),
    # path('<int:id>/update/',EmployeeUpdateView.as_view(),name='employee-update')
]
