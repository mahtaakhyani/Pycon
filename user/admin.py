from django.contrib import admin

# Register your models here.


from user.models import *
from upload.models import *

admin.site.register(CustomUser)
admin.site.register(CustomUserUpload)
admin.site.register(File)