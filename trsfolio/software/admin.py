from django.contrib import admin
from .models import *


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(ProjectDetails)
class ProjectDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(Collaborators)
class CollaboratorsAdmin(admin.ModelAdmin):
    pass

