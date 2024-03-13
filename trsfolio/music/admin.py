from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import *




admin.site.register(Venue)
admin.site.register(Artist)
admin.site.register(Ep)
admin.site.register(Event)

