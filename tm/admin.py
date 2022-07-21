from django import forms
from django.contrib import admin

from .models import Task


class TaskAdminForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "deadline")
    list_filter = ("owner", "deadline")
    search_fields = ("owner", "name")
    save_on_top = True
    save_as = True
    form = TaskAdminForm


admin.site.site_title = "Task Manager"
admin.site.site_header = "Task Manager"
