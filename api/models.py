from django.db import models

class MyFiles(models.Model):
	file = models.FileField(upload_to='uploaded_files')
