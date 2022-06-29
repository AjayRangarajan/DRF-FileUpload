from django.urls import path, include
from api.views import FileUploadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('upload_files', FileUploadViewSet, basename='upload_files')

urlpatterns = [
	path('', include(router.urls)),
]

