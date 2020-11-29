from django.contrib import admin
from school.models import Student


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'document')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Student, Students)
