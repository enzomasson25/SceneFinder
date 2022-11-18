from django.contrib import admin
from .models import Comment, Video, Sequence
# Register your models here.


admin.site.register(Comment)
admin.site.register(Video)
admin.site.register(Sequence)