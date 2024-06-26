from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from citysound.users.api.views import UserViewSet
from citysound.tours.api.views import TourViewSet, TourStopViewSet, TourCommentViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("tours", TourViewSet, TourStopViewSet)
router.register(r"tours/(?P<tour_id>[^/.]+)/stops", TourStopViewSet, basename='tour-stops')
router.register(r"tours/(?P<tour_id>[^/.]+)/comments", TourCommentViewSet, basename='tour-comments')

app_name = "api"
urlpatterns = router.urls
