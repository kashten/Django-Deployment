from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include


from django.views.generic.base import RedirectView
from rest_framework import routers
from titanic import views
#from rest_framework_jwt.views import obtain_jwt_token

router = routers.DefaultRouter()
router.register(r'titanic', views.TitanicViewSet)
#router.register(r'auth', views.UserViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('',RedirectView.as_view(url='api/')),
    
    #url(r'api-token-auth/', obtain_jwt_token),
]
