from django.urls import path
from Portfolio.views import PerfilListView
from .router import router


urlpatterns= [
    path('', PerfilListView.as_view()),
]

urlpatterns += router.urls
