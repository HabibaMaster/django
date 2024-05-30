from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from.models import Post

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    list_display=('title','slug','status','created_on')
    list_filter=['status']
    search_fields=['title','content']
    summernote_fields = ('content',)
    prepopulated_field={'slug':('title',)}


admin.site.register(Post,PostAdmin)


