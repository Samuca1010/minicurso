from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
	list_display="nome","sobrenome","curso"
admin.site.register(Member,MemberAdmin)
