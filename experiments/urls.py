from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExperimentViewSet, PopulationViewSet, IndividualViewSet, GameIterationViewSet

router = DefaultRouter()
router.register(r'experiments', ExperimentViewSet)
router.register(r'populations', PopulationViewSet)
router.register(r'individuals', IndividualViewSet)
router.register(r'gameiterations', GameIterationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
