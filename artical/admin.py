from django.contrib import admin
from .models import *
# Register your models here.

class ArticalAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','tags','publish_date','expiration_date','item','is_activate')
    list_filter = ('title','author','status','tags','publish_date','expiration_date')
    list_per_page = 25
    search_fields = ('title','author','status','tags')

    class Media:
        js = ('/static/ueditor/ueditor.config.js', '/static/ueditor/ueditor.all.min.js',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name','artical_count')

    def artical_count( self,obj ):
        return Artical.objects.filter(tags=obj).count()

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','item_count')

    def item_count( self,obj ):
        return Category.objects.filter(item_category=obj).count()

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'categorys', 'completed')

class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic', 'adurl', 'adlocation','status')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Artical,ArticalAdmin)
admin.site.register(Ad,AdAdmin)