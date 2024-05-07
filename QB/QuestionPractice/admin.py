from django.contrib import admin
from .models import *

# admin.site.register(Subject)
# admin.site.register(Question)
# admin.site.register(Option)

@admin.register(Subject)
class Subjectadmin(admin.ModelAdmin):
    list_display=('id','name')

#
@admin.register(Question)
class Questionadmin(admin.ModelAdmin):
    list_display=('id','question_text','subject')

@admin.register(Option)
class Optionadmin(admin.ModelAdmin):
    list_display=('id','text','question','is_correct')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
