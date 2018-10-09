from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import Index, AddWidget

urlpatterns = [
    path('', login_required(Index.as_view()), name="home"),
    path('addWidget/', login_required(AddWidget.as_view()), name="addWidget")
]
