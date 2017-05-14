from django.contrib import admin
# Register your models here.
from .models import userInfo, insertCode, Query, Code, newCode, Feedback, Code_Query, User_Search

class UserAdmin(admin.ModelAdmin):
	list_display=('first_name', 'last_name', 'email')
	search_fields=('first_name', 'last_name', 'username')

class QueryAdmin(admin.ModelAdmin):
	list_display=('application',)

admin.site.register(userInfo)
admin.site.register(Query, QueryAdmin)
admin.site.register(User_Search)
admin.site.register(Code)
admin.site.register(Feedback)
admin.site.register(newCode)
admin.site.register(insertCode)
admin.site.register(Code_Query)
