from django.urls import path

from . import views

app_name = 'DIYtour'

urlpatterns = [
    path('', views.index, name='index'),
]

handler404 = 'basis.views.page_not_found'