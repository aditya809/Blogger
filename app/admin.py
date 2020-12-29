from django.contrib import admin

# Register your models here.
from .models import SocialLink
from .models import Blogs

# from .models import TopicContent

# Register your models here.
admin.site.register(SocialLink)
admin.site.register(Blogs)
# sadmin.site.register(TopicContent)