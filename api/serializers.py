from rest_framework import serializers
from api.models import MyFiles

class FilesUploadSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyFiles
		fields = '__all__'