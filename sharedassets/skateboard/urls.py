from rest_framework.routers import DefaultRouter
from django.urls import include,path
from skateboard import views


router = DefaultRouter()
router.register(r'skateboard', views.SkateBoardViewSet,basename="skateboard")


urlpatterns = [
    path('api/', include(router.urls)),
	
]
