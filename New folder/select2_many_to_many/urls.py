from dal import autocomplete

from django.conf.urls import path
from django.views import generic

from .forms import TForm
from .models import TModel
from .views import UpdateView

app_name='select2_many_to_many'
urlpatterns = [
    path(
        'test-autocomplete/$',
        autocomplete.Select2QuerySetView.as_view(
            model=TModel,
            create_field='name',
        ),
        name='select2_many_to_many_autocomplete',
    ),
    path(
        'test/(?P<pk>\d+)/$',
        generic.UpdateView.as_view(
            model=TModel,
            form_class=TForm,
        )
    ),
    path(
        '',
        UpdateView.as_view(),
        name='select2_outside_admin',
    ),
]
