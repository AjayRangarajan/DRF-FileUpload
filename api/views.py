from rest_framework.viewsets import ModelViewSet
from api.models import MyFiles
from api.serializers import FilesUploadSerializer

class FileUploadViewSet(ModelViewSet):
	queryset = MyFiles.objects.all()
	serializer_class = FilesUploadSerializer