from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
# customizing are models in admin panel


class TutorialAdmin(admin.ModelAdmin):
    # fields = ['tutorial_published',
    #           "tutorial_title",
    #           "tutorial_content",
    #           ]
    fieldsets = [
        ("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Tutorial, TutorialAdmin)
