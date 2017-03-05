from django.contrib import admin
# Register your models here.
from .models import userInfo, insertCode, Query, Code, newCode, Feedback, Code_Query

class UserAdmin(admin.ModelAdmin):
	list_display=('first_name', 'last_name', 'email')
	search_fields=('first_name', 'last_name')

class QueryAdmin(admin.ModelAdmin):
	list_display=('query_text',)

admin.site.register(Query, QueryAdmin)
admin.site.register(Code)
admin.site.register(Feedback)
admin.site.register(newCode)
admin.site.register(insertCode)
admin.site.register(Code_Query)
