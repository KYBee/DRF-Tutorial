from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns([

#     # function view
#     #path('snippets/', views.snippet_list),
#     #path('snippets/<int:pk>/', views.snippet_detail),

#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view({
#         'get': 'highlight'
#     }), name="snippet-highlight"),

#     # class view
#     path('snippets/', views.SnippetList.as_view({
#         'get': 'list',
#         'post': 'create',
#     }), name="snippet-list"),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view({
#         'get' : 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name="snippet-detail"),

#     path("users/", views.UserList.as_view({
#         'get': 'list'
#     }), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view({
#         'get': 'retrieve'
#     }), name='user-detail'),

# ])
