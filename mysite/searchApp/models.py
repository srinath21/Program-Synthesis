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
	application=models.CharField(max_length=20, blank=False)
	function=models.CharField(max_length=20, blank=True)
	language=models.CharField(max_length=20, blank=False)
	app_description=models.TextField(blank=False)
	function_description=models.TextField(blank=False)
	def __str__(self):
		return str(self.id)

class Code(models.Model):
	code_text=models.TextField(max_length=20000, blank=False)
	user=models.ForeignKey(User)
	def __str__(self):
		return str(self.id)

class Code_Query(models.Model):
	query=models.OneToOneField(Query)
	code=models.OneToOneField(Code)

class User_Search(models.Model):
	user=models.ForeignKey(User)
	query=models.ForeignKey(Query)
	code=models.ForeignKey(Code)

class insertCode(models.Model):
    user=models.OneToOneField(User)
    query=models.OneToOneField(Query)
    codeText=models.TextField()
    codeReview=models.BooleanField()

    def __str__(self):
        return self.user.username
class Feedback(models.Model):
	feedback_info=models.TextField(max_length=10000)
	user=models.ForeignKey(User)
	query=models.ForeignKey(Query)
	def __str__(self):
		return str(User.id)

class newCode(models.Model):
	user=models.ForeignKey(User)
	query_name=models.CharField(max_length=100)
	code_text=models.TextField()
	code_review=models.TextField()

	def __str__(self):
		return self.query_name and self.user
