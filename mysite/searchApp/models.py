from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userInfo(models.Model):
	user=models.OneToOneField(User)
	age=models.IntegerField(default=0)
	country=models.CharField(max_length=15)

	def __str__(self):
		return self.first_name and self.last_name

class Query(models.Model):
	query_text=models.CharField(max_length=20, blank=False)

	def __str__(self):
		return self.query_text

class Code(models.Model):
	code_text=models.TextField(max_length=20000, blank=False)

	def __str__(self):
		return str(self.id)

class Code_Query(models.Model):
	query=models.OneToOneField(Query)
	code=models.OneToOneField(Code)

class insertCode(models.Model):
    user=models.OneToOneField(User)
    query=models.OneToOneField(Query)
    codeText=models.TextField()
    codeReview=models.TextField()

    def __str__(self):
        return self.user and self.query
class Feedback(models.Model):
	feedback_info=models.TextField(max_length=10000)
	user=models.ForeignKey(User)
	
	def __str__(self):
		return str(User.id)

class newCode(models.Model):
	user=models.ForeignKey(User)
	query_name=models.CharField(max_length=100)
	code_text=models.TextField()
	code_review=models.TextField()

	def __str__(self):
		return self.query_name and self.user
