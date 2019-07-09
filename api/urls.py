from rest_framework import routers
from django.conf.urls import url
from cardstock import views

router = routers.DefaultRouter()
router.register('cards', views.CardViewSet)

urlpatterns = [
    url(r'^cards/(?P<card_type>\w+)/$', views.CardViewSet.as_view({'get': 'card_type_cards'}), name='card_type_cards')
]
urlpatterns += router.urls
