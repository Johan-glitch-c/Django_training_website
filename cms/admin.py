from django.contrib import admin
from .models import CmsSlider
from django.utils.safestring import mark_safe
# Register your models here.



class CmsAdm(admin.ModelAdmin):
    list_display=("cms_title","cms_text","cms_css","get_image",)
    list_display_links=("cms_title",)
    list_editable=("cms_css",)
    fields=("cms_title","cms_text","cms_css","cms_img" ,"get_image",)
    readonly_fields=("get_image",)


    def get_image(self,obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80" ')
        else:
            return "No image"

    get_image.short_description= "Miniature"
admin.site.register(CmsSlider,CmsAdm)