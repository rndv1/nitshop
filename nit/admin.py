from django.contrib import admin
from blog.models import Article
from nit.models import Contact

admin.site.register(Article)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
