from django.urls import path
from .views import *

urlspatterns = [
    path('snippets/', snippet_list),
    path('snippets/<int:pk>', snippet_detail),
]

