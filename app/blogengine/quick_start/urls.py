from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups',GroupViewSet)



urlpatterns = [
      path('', test, name='test'),
      path('api-auth/', include('rest_framework.urls', namespace= 'rest_framework')),
      path('snippets/', snippet_list, name = 'snippet_list'),
      path('snippets/<int:pk>/',snippet_detail, name = 'snippet_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)