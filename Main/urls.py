from django.urls import path
from . import views as Main_Views

urlpatterns = [
    path('', Main_Views.home_view, name='home'),
    path('market/', Main_Views.marketplace, name='market'),
    path('coming/', Main_Views.coming, name='coming'),
]
