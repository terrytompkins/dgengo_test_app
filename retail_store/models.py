from django.db import models
class MyModel(models.Model):
	id = models.AutoField(primary_key=true)
	name = models.CharField(max_length=100, unique=true, blank=false, null=false)
	created_at = models.DateTimeField(auto_now_add=true)
	updated_at = models.DateTimeField(auto_now=true)
	related_model = models.ForeignKey(to='RelatedModel', related_name='my_model', on_delete=models.CASCADE)
    
	class Meta:
		ordering = -created_at
		verbose_name = 'My Model'
	
		def __str__(self):
			return self.id
class RelatedModel(models.Model):
	id = models.AutoField(primary_key=true)
	info = models.TextField(blank=true)
	
	class Meta:
	
		def __str__(self):
			return self.id

