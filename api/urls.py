from rest_framework import routers
from cardstock import views

router = routers.DefaultRouter()
router.register('cards', views.CardViewSet)
urlpatterns = router.urls
